import json
from datetime import timedelta
from pathlib import Path

from django.conf import settings
from django.db.models import Count
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_GET, require_POST

from . import ai
from .airdata import get_data, invalidate, level_for
from .models import AdviceLog, CitizenReport, District
from .translations import GROUPS, strings

APK_PATH = Path(settings.BASE_DIR) / "static" / "downloads" / "AralShield.apk"


# ------------------------------------------------------------------ helpers

def _rows(lang, demo=False):
    """District list joined with live data, sorted by current risk (desc)."""
    data = get_data(demo=demo)
    since = timezone.now() - timedelta(hours=24)
    counts = dict(
        CitizenReport.objects.filter(created_at__gte=since)
        .values_list("district__slug").annotate(n=Count("id"))
    )
    rows = []
    for d in District.objects.all():
        dd = data["districts"].get(d.slug) or {}
        cur = dd.get("current") or {}
        rows.append({
            "d": d,
            "slug": d.slug,
            "name": d.name(lang),
            "cur": cur,
            "risk": cur.get("risk", 0),
            "level": cur.get("level", "low"),
            "color": cur.get("color", "#2fbf71"),
            "peak": dd.get("peak") or {},
            "reports24": counts.get(d.slug, 0),
        })
    rows.sort(key=lambda r: r["risk"], reverse=True)
    return data, rows


def _summary(rows):
    high = [r for r in rows if r["risk"] >= 40]
    return {
        "worst": rows[0] if rows else None,
        "n_high": len(high),
        "people_high": sum(r["d"].population for r in high),
        "n_total": len(rows),
        "max_peak": max((r["peak"].get("risk", 0) for r in rows), default=0),
    }


def _context_text(data, lang):
    parts = []
    for d in District.objects.all():
        dd = data["districts"].get(d.slug)
        if dd:
            parts.append(ai.describe_district(d.name_en, dd))
    note = " (SIMULATED DATA — source offline)" if data.get("simulated") else ""
    return f"Generated {data.get('generated_at')}{note}\n" + "\n".join(parts)


# ------------------------------------------------------------------ pages

def home(request):
    data, rows = _rows(request.lang, request.demo)
    return render(request, "home.html", {
        "data": data, "rows": rows, "s": _summary(rows), "nav": "home",
        "map_json": json.dumps([
            {"slug": r["slug"], "name": r["name"], "lat": r["d"].lat, "lon": r["d"].lon,
             "risk": r["risk"], "color": r["color"], "level": r["level"]} for r in rows
        ], ensure_ascii=False),
    })


def districts(request):
    data, rows = _rows(request.lang, request.demo)
    return render(request, "districts.html", {"data": data, "rows": rows, "nav": "districts"})


def district_detail(request, slug):
    d = get_object_or_404(District, slug=slug)
    data = get_data(demo=request.demo)
    dd = data["districts"].get(slug)
    if not dd:
        raise Http404
    cur = dd["current"]
    hourly = dd["hourly"]
    chart = {
        "labels": [h["time"][5:16].replace("T", " ") for h in hourly],
        "risk": [h["risk"] for h in hourly],
        "pm10": [h["pm10"] for h in hourly],
        "dust": [h["dust"] for h in hourly],
        "wind": [h["wind"] for h in hourly],
    }
    reports = CitizenReport.objects.filter(district=d)[:8]
    t = strings(request.lang)
    parts = [(t["part_" + k], v) for k, v in (cur.get("parts") or {}).items()]
    return render(request, "district.html", {
        "d": d, "name": d.name(request.lang), "cur": cur, "peak": dd["peak"], "data": data,
        "chart_json": json.dumps(chart), "reports": reports, "parts": parts,
        "groups": GROUPS, "nav": "districts",
        "all": District.objects.all(),
    })


def assistant(request):
    return render(request, "assistant.html", {"nav": "assistant", "ai_on": ai.ai_enabled()})


def report(request):
    t = strings(request.lang)
    sent = request.GET.get("sent") == "1"
    error = None
    if request.method == "POST":
        try:
            district = District.objects.get(slug=request.POST.get("district"))
            kind = request.POST.get("kind")
            severity = int(request.POST.get("severity", 3))
            if kind not in dict(CitizenReport.KIND_CHOICES) or not 1 <= severity <= 5:
                raise ValueError
            CitizenReport.objects.create(
                district=district, kind=kind, severity=severity,
                comment=(request.POST.get("comment") or "")[:300],
            )
            invalidate()
            return redirect(f"/report/?sent=1&d={district.slug}")
        except (District.DoesNotExist, ValueError, TypeError):
            error = t["report_error"]
    since = timezone.now() - timedelta(hours=24)
    latest = CitizenReport.objects.filter(created_at__gte=since).select_related("district")[:30]
    return render(request, "report.html", {
        "nav": "report", "sent": sent, "error": error, "latest": latest,
        "all": District.objects.all(), "preselect": request.GET.get("d", ""),
        "kinds": [("dust", t["kind_dust"]), ("salt", t["kind_salt"]),
                  ("visibility", t["kind_visibility"]), ("health", t["kind_health"])],
    })


def dashboard(request):
    data, rows = _rows(request.lang, request.demo)
    t = strings(request.lang)
    for r in rows:
        r["action"] = t["act_" + r["level"]]
        r["peak_color"] = r["peak"].get("color", "#2fbf71")
    return render(request, "dashboard.html", {"data": data, "rows": rows, "s": _summary(rows), "nav": "dashboard"})


def about(request):
    return render(request, "about.html", {"nav": "about"})


def download(request):
    return render(request, "download.html", {
        "nav": "download", "apk_ready": APK_PATH.exists(),
        "apk_size": round(APK_PATH.stat().st_size / 1024 / 1024, 1) if APK_PATH.exists() else 0,
        "site_url": request.build_absolute_uri("/download/"),
    })


# ------------------------------------------------------------------ API

def _cors(resp):
    resp["Access-Control-Allow-Origin"] = "*"
    return resp


@require_GET
def api_risk(request):
    lang = request.GET.get("lang", request.lang)
    data, rows = _rows(lang, request.GET.get("demo") == "1")
    only = request.GET.get("district")
    out = []
    for r in rows:
        if only and r["slug"] != only:
            continue
        c = r["cur"]
        out.append({
            "slug": r["slug"], "name": r["name"], "lat": r["d"].lat, "lon": r["d"].lon,
            "risk": r["risk"], "level": r["level"], "color": r["color"],
            "level_name": strings(lang)["lvl_" + r["level"]],
            "pm10": c.get("pm10"), "pm25": c.get("pm25"), "dust": c.get("dust"),
            "wind": c.get("wind"), "wind_dir": c.get("wind_dir"), "humidity": c.get("rh"),
            "salt_probability": c.get("salt"), "from_aralkum": c.get("from_aralkum"),
            "peak_72h": r["peak"], "reports_24h": r["reports24"],
        })
    return _cors(JsonResponse({
        "generated_at": data["generated_at"], "simulated": data["simulated"], "demo": data.get("demo", False),
        "source": "Open-Meteo / Copernicus CAMS", "index": "Aral Dust Risk Index (0-100)",
        "districts": out,
    }, json_dumps_params={"ensure_ascii": False}))


@require_GET
def api_district(request, slug):
    get_object_or_404(District, slug=slug)
    data = get_data(demo=request.GET.get("demo") == "1")
    return _cors(JsonResponse({"simulated": data["simulated"], **data["districts"][slug]}))


def _json_body(request):
    try:
        return json.loads(request.body or b"{}")
    except ValueError:
        return {}


@require_POST
def api_advice(request):
    body = _json_body(request)
    lang = body.get("lang") if body.get("lang") in ("qq", "uz", "ru", "en") else request.lang
    group = body.get("group") if body.get("group") in GROUPS else "general"
    try:
        d = District.objects.get(slug=body.get("district"))
    except District.DoesNotExist:
        return JsonResponse({"error": "district"}, status=400)
    data = get_data(demo=request.demo)
    dd = data["districts"][d.slug]
    level = (dd.get("current") or {}).get("level", "moderate")
    text, model, fallback = ai.personal_advice(ai.describe_district(d.name_en, dd), level, group, lang)
    AdviceLog.objects.create(kind="advice", lang=lang, question=f"{d.slug}/{group}", answer=text, model_used=model)
    return JsonResponse({"answer": text, "model": model, "fallback": fallback})


@require_POST
def api_chat(request):
    body = _json_body(request)
    lang = body.get("lang") if body.get("lang") in ("qq", "uz", "ru", "en") else request.lang
    history = body.get("messages") or []
    if not isinstance(history, list) or not history:
        return JsonResponse({"error": "empty"}, status=400)
    data, rows = _rows(lang, request.demo)
    question = str(history[-1].get("content", ""))[:1500]
    t = strings(lang)
    try:
        text, model = ai.chat(history, _context_text(data, lang), lang)
    except Exception:
        text, model = None, "rules"
    fallback = text is None
    if fallback:
        top = rows[:3]
        lines = [f"{t['worst_now']}:"] + [
            f"• {r['name']} — {r['risk']}/100 ({t['lvl_' + r['level']]})" for r in top
        ]
        worst_level = top[0]["level"] if top else "low"
        text = "\n".join(lines) + "\n\n" + ai.rule_advice(worst_level, "general", lang)
    AdviceLog.objects.create(kind="chat", lang=lang, question=question, answer=text, model_used=model)
    return JsonResponse({"answer": text, "model": model, "fallback": fallback})


@require_GET
def api_health(request):
    return JsonResponse({"ok": True, "ai": ai.ai_enabled(), "districts": District.objects.count()})


def level_name(lang, score):
    return strings(lang)["lvl_" + level_for(score)[0]]
