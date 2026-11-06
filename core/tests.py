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

    def test_history_page(self):
        from django.core.cache import cache
        cache.clear()
        n = District.objects.count()
        start = timezone.localtime().replace(hour=0, minute=0) - timezone.timedelta(days=3)
        times = [(start + timezone.timedelta(hours=h)).strftime("%Y-%m-%dT%H:00") for h in range(96)]
        pm = [40.0] * 96
        pm[30] = 260.0  # a real-looking spike on day 2
        air = [{"hourly": {"time": times, "pm10": pm, "pm2_5": [12.0] * 96, "dust": [30.0] * 96}} for _ in range(n)]
        wx = [{"hourly": {"time": times, "wind_speed_10m": [9.0] * 96, "wind_direction_10m": [350] * 96,
                          "relative_humidity_2m": [25] * 96}} for _ in range(n)]
        with mock.patch("core.airdata.requests.get", side_effect=[fake_resp(air), fake_resp(wx)]):
            h = airdata.get_history()
        self.assertTrue(h["ok"])
        rows = h["districts"]["moynaq"]
        self.assertEqual(len(rows), 3)  # 3 past days, today excluded
        self.assertEqual(max(r["max_pm10"] for r in rows), 260)
        self.assertEqual(h["worst"]["slug"], "moynaq")
        for lang in ("qq", "uz", "ru", "en"):
            r = self.client.get(f"/history/?d=kungrad&lang={lang}")
            self.assertEqual(r.status_code, 200)
            self.assertContains(r, "open-meteo.com")
        self.assertEqual(self.client.get("/api/history/moynaq/").json()["days"][0]["date"], rows[0]["date"])

    def test_history_offline_is_honest(self):
        from django.core.cache import cache
        cache.clear()
        with mock.patch("core.airdata.requests.get", side_effect=OSError("offline")):
            r = self.client.get("/history/?lang=qq")
        self.assertEqual(r.status_code, 200)
        self.assertContains(r, "jalǵanıw múmkin bolmadı")

    def test_ensure_admin(self):
        from django.contrib.auth import get_user_model
        from django.core.management import call_command
        call_command("ensure_admin")
        u = get_user_model().objects.get(username="admin")
        self.assertTrue(u.is_superuser and u.check_password("admin123"))
        u.set_password("changed"); u.save()
        call_command("ensure_admin")  # must not reset a changed password
        self.assertTrue(get_user_model().objects.get(username="admin").check_password("changed"))
