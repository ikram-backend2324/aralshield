from unittest import mock

from django.test import TestCase
from django.utils import timezone

from . import airdata
from .districts import seed_districts
from .models import District


def fake_resp(payload):
    m = mock.Mock()
    m.json.return_value = payload
    m.raise_for_status.return_value = None
    return m


class OpenMeteoParsing(TestCase):
    def setUp(self):
        seed_districts()

    def test_parse_multi_location(self):
        n = District.objects.count()
        now = timezone.localtime().replace(minute=0)
        times = [(now.replace(hour=0) + timezone.timedelta(hours=h)).strftime("%Y-%m-%dT%H:00") for h in range(72)]
        air = [{"hourly": {"time": times, "pm10": [300.0] * 72, "pm2_5": [80.0] * 72, "dust": [400.0] * 72,
                           "aerosol_optical_depth": [0.9] * 72, "us_aqi": [180] * 72}} for _ in range(n)]
        wx = [{"hourly": {"time": times, "wind_speed_10m": [12.0] * 72, "wind_direction_10m": [340] * 72,
                          "relative_humidity_2m": [20] * 72, "temperature_2m": [15.0] * 72,
                          "visibility": [2000] * 72}} for _ in range(n)]
        with mock.patch("core.airdata.requests.get", side_effect=[fake_resp(air), fake_resp(wx)]):
            data = airdata.get_data(force=True)
        self.assertFalse(data["simulated"])
        moynaq = data["districts"]["moynaq"]["current"]
        self.assertGreaterEqual(moynaq["risk"], 95)
        self.assertEqual(moynaq["level"], "extreme")
        self.assertTrue(moynaq["from_aralkum"])
        turtkul = data["districts"]["turtkul"]["current"]
        self.assertLess(turtkul["risk"], moynaq["risk"])
        self.assertTrue(len(data["districts"]["nukus"]["hourly"]) > 0)

    def test_fallback_simulation(self):
        with mock.patch("core.airdata.requests.get", side_effect=OSError("offline")):
            data = airdata.get_data(force=True)
        self.assertTrue(data["simulated"])
        self.assertEqual(len(data["districts"]), District.objects.count())

    def test_risk_bounds(self):
        s, salt, parts = airdata.compute_risk(0, 0, 0, 0, 180, 90, 300)
        self.assertEqual(s, 0)
        s, salt, parts = airdata.compute_risk(1000, 500, 2000, 30, 0, 5, 10, 50)
        self.assertEqual(s, 100)
