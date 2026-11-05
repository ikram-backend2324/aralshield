"""OpenRouter integration with a safe rule-based fallback."""
import logging

import requests
from django.conf import settings

from .translations import GROUP_ADVICE, LANG_NAMES_EN, LEVEL_ADVICE

log = logging.getLogger(__name__)
URL = "https://openrouter.ai/api/v1/chat/completions"

SYSTEM = (
    "You are AralShield, an air-quality and health-protection assistant for the Republic of "
    "Karakalpakstan (Uzbekistan), where salt-dust storms blow from the Aralkum desert (the dried "
    "Aral Sea bed). You receive live hourly data and the Aral Dust Risk Index (ADRI, 0-100; "
    "<20 low, 20-40 moderate, 40-60 high, 60-80 very high, 80+ extreme). "
    "Rules: answer ONLY in {lang_name}. {script_rule} Be concrete, warm and short (max ~140 words "
    "unless asked for more), use simple bullet points when listing actions. Base statements about "
    "current conditions strictly on the data provided; if data is missing, say so. Never diagnose "
    "disease or prescribe medication doses; for severe symptoms tell people to call 103 "
    "(ambulance in Uzbekistan). Do not invent statistics. "
    "Match the strength of your advice to the risk level: at LOW risk say clearly that normal "
    "activities are fine and give at most 1-2 light tips; only recommend masks, closed windows or "
    "staying indoors when the level is HIGH or above (or when the forecast peak is). "
    "Use plain text only: no markdown, no asterisks, no bold; start list lines with '• '. "
    "Current local date and time in Nukus: {now}. Use it for words like today/tomorrow."
)
SCRIPT_RULES = {
    "qq": "Write in modern Karakalpak Latin alphabet (letters á, ó, ú, ı, ń, ǵ), not Uzbek and not Kazakh.",
    "uz": "Write in Uzbek Latin script (o', g', sh, ch).",
    "ru": "",
    "en": "",
}


def ai_enabled():
    return bool(settings.OPENROUTER_API_KEY)


def _call(messages, max_tokens=500):
    models = [settings.OPENROUTER_MODEL] + [m for m in settings.OPENROUTER_FALLBACK_MODELS
                                            if m != settings.OPENROUTER_MODEL]
    last_err = None
    for model in models:
        try:
            r = requests.post(
                URL,
                headers={
                    "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
                    "HTTP-Referer": settings.SITE_URL,
                    "X-Title": "AralShield",
                    "Content-Type": "application/json",
                },
                json={"model": model, "messages": messages, "max_tokens": max_tokens, "temperature": 0.4},
                timeout=45,
            )
            if r.status_code != 200:
                last_err = f"{model}: HTTP {r.status_code} {r.text[:200]}"
                log.warning("OpenRouter error %s", last_err)
                continue
            j = r.json()
            text = (j.get("choices") or [{}])[0].get("message", {}).get("content") or ""
            if text.strip():
                return clean(text), j.get("model", model)
            last_err = f"{model}: empty answer"
        except Exception as exc:  # network etc.
            last_err = f"{model}: {exc}"
            log.warning("OpenRouter exception %s", last_err)
    raise RuntimeError(last_err or "AI unavailable")


def system_prompt(lang):
    from django.utils import timezone
    now = timezone.localtime().strftime("%Y-%m-%d %H:%M (%A)")
    return SYSTEM.format(lang_name=LANG_NAMES_EN.get(lang, "English"), script_rule=SCRIPT_RULES.get(lang, ""), now=now)


def clean(text):
    """Remove markdown the UI cannot render (bold, headings, '*' bullets)."""
    import re
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"(?m)^\s*[\*\-]\s+", "• ", text)
    text = re.sub(r"(?m)^#+\s*", "", text)
    return text.replace("**", "").strip()


def describe_district(name, d):
    c = d.get("current") or {}
    p = d.get("peak") or {}
    return (
        f"{name}: ADRI now {c.get('risk')} ({c.get('level')}), PM10 {c.get('pm10')} µg/m³, "
        f"PM2.5 {c.get('pm25')} µg/m³, dust {c.get('dust')} µg/m³, wind {c.get('wind')} m/s from "
        f"{c.get('wind_dir')}°{' (from Aralkum)' if c.get('from_aralkum') else ''}, humidity {c.get('rh')}%, "
        f"Aralkum salt-dust probability {c.get('salt')}%; 72h peak ADRI {p.get('risk')} at {p.get('time')}."
    )


def rule_advice(level, group, lang):
    base = LEVEL_ADVICE.get(level, LEVEL_ADVICE["moderate"])[lang]
    extra = "" if level == "low" else GROUP_ADVICE.get(group, GROUP_ADVICE["general"])[lang]
    return (base + ("\n\n" + extra if extra else "")).strip()


def personal_advice(district_text, level, group, lang):
    if not ai_enabled():
        return rule_advice(level, group, lang), "rules", True
    user = (
        f"Live data: {district_text}\nPerson profile: {group}.\n"
        "Give personal protection advice for the next 24 hours: 1 sentence on the situation, then "
        "bullet actions specific to this profile (1-2 if risk is low, 3-5 if high or above), "
        "then 1 line on when to seek medical help."
    )
    try:
        text, model = _call([
            {"role": "system", "content": system_prompt(lang)},
            {"role": "user", "content": user},
        ])
        return text, model, False
    except Exception:
        return rule_advice(level, group, lang), "rules", True


def chat(history, context_text, lang):
    if not ai_enabled():
        return None, "rules"
    msgs = [{"role": "system", "content": system_prompt(lang) + "\n\nLIVE DATA (all districts):\n" + context_text}]
    for m in history[-10:]:
        role = "assistant" if m.get("role") == "assistant" else "user"
        content = str(m.get("content", ""))[:1500]
        if content:
            msgs.append({"role": role, "content": content})
    return _call(msgs, max_tokens=700)
