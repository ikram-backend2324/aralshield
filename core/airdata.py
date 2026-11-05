"""Atmospheric data + Aral Dust Risk Index (ADRI).

Data source: Open-Meteo Air Quality API (CAMS / Copernicus atmosphere model) and
Open-Meteo Weather API. Both are free and need no API key.
If the network is unavailable, the last saved snapshot is used; if there is none,
a clearly-flagged simulation is generated so the demo never breaks.
"""
import logging
import math
from datetime import datetime, timedelta

import requests
from django.conf import settings
from django.core.cache import cache
from django.utils import timezone

from .models import CitizenReport, District, Snapshot

log = logging.getLogger(__name__)

AIR_URL = "https://air-quality-api.open-meteo.com/v1/air-quality"
WX_URL = "https://api.open-meteo.com/v1/forecast"
CACHE_KEY = "aral_snapshot_v2"

# Wind blowing FROM this sector (degrees) comes from the dried Aral seabed (Aralkum)
ARALKUM_SECTOR = (290, 60)

LEVELS = [
    (20, "low", "#2fbf71"),
    (40, "moderate", "#e3c34a"),
    (60, "high", "#f08a24"),
    (80, "very_high", "#e04b3c"),
    (101, "extreme", "#8e2bd6"),
]


def level_for(score):
    for limit, key, color in LEVELS:
        if score < limit:
            return key, color
    return "extreme", "#8e2bd6"


def _clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


def from_aralkum(direction):
    if direction is None:
        return False
    a, b = ARALKUM_SECTOR
    d = direction % 360
    return d >= a or d <= b


def compute_risk(pm10, pm25, dust, wind, wind_dir, rh, km_to_aralkum, report_boost=0.0):
    """Aral Dust Risk Index 0..100 plus component breakdown."""
    pm10 = pm10 or 0.0
    pm25 = pm25 or 0.0
    dust = dust or 0.0
    wind = wind or 0.0
    rh = 50.0 if rh is None else rh
    proximity = _clamp(1 - km_to_aralkum / 400.0, 0.1, 1.0)
    sector = from_aralkum(wind_dir)
    wind_factor = _clamp((wind - 4.0) / 8.0) * (1.0 if sector else 0.35)

    parts = {
        "pm10": min(pm10 / 250.0, 1) * 40,
        "pm25": min(pm25 / 75.0, 1) * 15,
        "dust": min(dust / 300.0, 1) * 20,
        "wind": 15 * wind_factor * (0.5 + 0.5 * proximity),
        "dry": 5.0 if rh < 30 else (2.5 if rh < 45 else 0.0),
        "reports": min(report_boost, 10.0),
    }
    score = int(round(_clamp(sum(parts.values()), 0, 100)))
    salt_prob = int(round(100 * (1.0 if sector else 0.15) * _clamp(wind / 10.0) * proximity))
    return score, salt_prob, {k: round(v, 1) for k, v in parts.items()}


# ---------------------------------------------------------------- fetching

def _fetch_open_meteo(districts):
    lats = ",".join(f"{d.lat:.4f}" for d in districts)
    lons = ",".join(f"{d.lon:.4f}" for d in districts)
    common = {"latitude": lats, "longitude": lons, "timezone": "Asia/Tashkent", "forecast_days": 3}
    air = requests.get(
        AIR_URL,
        params={**common, "hourly": "pm10,pm2_5,dust,aerosol_optical_depth,us_aqi"},
        timeout=15,
    )
    air.raise_for_status()
    wx = requests.get(
        WX_URL,
        params={
            **common,
            "hourly": "wind_speed_10m,wind_direction_10m,relative_humidity_2m,temperature_2m,visibility",
            "wind_speed_unit": "ms",
        },
        timeout=15,
    )
    wx.raise_for_status()
    air_j, wx_j = air.json(), wx.json()
    if isinstance(air_j, dict):
        air_j = [air_j]
    if isinstance(wx_j, dict):
        wx_j = [wx_j]
    if len(air_j) != len(districts) or len(wx_j) != len(districts):
        raise ValueError("unexpected Open-Meteo response length")

    out = {}
    for d, a, w in zip(districts, air_j, wx_j):
        ah, wh = a.get("hourly", {}), w.get("hourly", {})
        times = ah.get("time", [])
        wx_index = {t: i for i, t in enumerate(wh.get("time", []))}
        rows = []
        for i, t in enumerate(times):
            j = wx_index.get(t)

            def g(src, key, idx):
                arr = src.get(key) or []
                return arr[idx] if idx is not None and idx < len(arr) else None

            rows.append({
                "time": t,
                "pm10": g(ah, "pm10", i),
                "pm25": g(ah, "pm2_5", i),
                "dust": g(ah, "dust", i),
                "aod": g(ah, "aerosol_optical_depth", i),
                "aqi": g(ah, "us_aqi", i),
                "wind": g(wh, "wind_speed_10m", j),
                "wind_dir": g(wh, "wind_direction_10m", j),
                "rh": g(wh, "relative_humidity_2m", j),
                "temp": g(wh, "temperature_2m", j),
                "vis": g(wh, "visibility", j),
            })
        out[d.slug] = rows
    return out


def _simulate(districts):
    """Deterministic, physically plausible simulation (used only when offline)."""
    now = timezone.localtime().replace(minute=0, second=0, microsecond=0)
    start = now.replace(hour=0)
    storm_day = (now.timetuple().tm_yday % 5) == 0
    out = {}
    for k, d in enumerate(districts):
        prox = _clamp(1 - d.distance_to_aralkum_km / 400.0, 0.1, 1.0)
        rows = []
        for h in range(72):
            t = start + timedelta(hours=h)
            diurnal = 0.5 + 0.5 * math.sin((t.hour - 9) / 24 * 2 * math.pi)
            wave = 0.5 + 0.5 * math.sin((h + k * 3) / 17.0)
            wind = 2 + 7 * diurnal * wave + (5 if storm_day and 10 <= h <= 30 else 0)
            wind_dir = (330 + 50 * math.sin((h + k) / 11.0)) % 360
            dust = (20 + 260 * prox * wave * diurnal) * (1.8 if storm_day and 10 <= h <= 30 else 1)
            pm10 = 25 + dust * 0.9 + 10 * wave
            rows.append({
                "time": t.strftime("%Y-%m-%dT%H:00"),
                "pm10": round(pm10, 1), "pm25": round(pm10 * 0.32, 1), "dust": round(dust, 1),
                "aod": round(0.15 + dust / 900, 2), "aqi": None,
                "wind": round(wind, 1), "wind_dir": round(wind_dir),
                "rh": round(55 - 30 * diurnal), "temp": round(8 + 10 * diurnal, 1), "vis": None,
            })
        out[d.slug] = rows
    return out


def _report_boosts():
    since = timezone.now() - timedelta(hours=3)
    boosts = {}
    for r in CitizenReport.objects.filter(created_at__gte=since).select_related("district"):
        boosts[r.district.slug] = boosts.get(r.district.slug, 0) + max(0, r.severity - 2) * 1.5
    return boosts


def _enrich(raw, districts, simulated):
    now_key = timezone.localtime().strftime("%Y-%m-%dT%H:00")
    boosts = _report_boosts()
    result = {"generated_at": timezone.now().isoformat(), "simulated": simulated, "districts": {}}
    for d in districts:
        rows = raw.get(d.slug, [])
        boost = boosts.get(d.slug, 0)
        for r in rows:
            r["risk"], r["salt"], _ = compute_risk(
                r["pm10"], r["pm25"], r["dust"], r["wind"], r["wind_dir"], r["rh"],
                d.distance_to_aralkum_km, 0,
            )
        # current hour
        idx = 0
        for i, r in enumerate(rows):
            if r["time"] <= now_key:
                idx = i
        cur = dict(rows[idx]) if rows else {}
        if cur:
            cur["risk"], cur["salt"], cur["parts"] = compute_risk(
                cur["pm10"], cur["pm25"], cur["dust"], cur["wind"], cur["wind_dir"], cur["rh"],
                d.distance_to_aralkum_km, boost,
            )
            cur["level"], cur["color"] = level_for(cur["risk"])
            cur["from_aralkum"] = from_aralkum(cur["wind_dir"])
        future = rows[idx: idx + 72]
        peak = max(future, key=lambda r: r["risk"]) if future else None
        result["districts"][d.slug] = {
            "current": cur,
            "hourly": future,
            "peak": {"time": peak["time"], "risk": peak["risk"], "level": level_for(peak["risk"])[0],
                     "color": level_for(peak["risk"])[1]} if peak else None,
            "report_boost": round(boost, 1),
        }
    return result


def get_data(force=False):
    if not force:
        cached = cache.get(CACHE_KEY)
        if cached:
            return cached
    districts = list(District.objects.all())
    if not districts:
        from .districts import seed_districts
        seed_districts()
        districts = list(District.objects.all())
    simulated = False
    try:
        raw = _fetch_open_meteo(districts)
        Snapshot.objects.create(payload=raw, simulated=False)
        Snapshot.objects.filter(
            id__in=list(Snapshot.objects.values_list("id", flat=True)[20:])
        ).delete()
    except Exception as exc:  # network / API problem
        log.warning("Open-Meteo fetch failed: %s", exc)
        snap = Snapshot.objects.filter(simulated=False,
                                       created_at__gte=timezone.now() - timedelta(hours=12)).first()
        if snap:
            raw = snap.payload
        else:
            raw = _simulate(districts)
            simulated = True
    data = _enrich(raw, districts, simulated)
    cache.set(CACHE_KEY, data, settings.DATA_CACHE_SECONDS if not simulated else 120)
    return data


def invalidate():
    cache.delete(CACHE_KEY)
