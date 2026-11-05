from .translations import LANGS, strings


def i18n(request):
    lang = getattr(request, "lang", "qq")
    in_app = request.GET.get("app") == "1" or "AralShieldApp" in request.META.get("HTTP_USER_AGENT", "")
    return {"t": strings(lang), "lang": lang, "langs": LANGS, "in_app": in_app}
