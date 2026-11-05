from django import template

register = template.Library()


@register.filter
def lvl(level, t):
    return t.get(f"lvl_{level}", level)


@register.filter
def tget(t, key):
    return t.get(key, key)


@register.filter
def num(v, digits=0):
    if v is None:
        return "—"
    try:
        return f"{float(v):.{int(digits)}f}"
    except (TypeError, ValueError):
        return v


@register.filter
def thousands(v):
    try:
        return f"{int(v):,}".replace(",", " ")
    except (TypeError, ValueError):
        return v


@register.filter
def pct(v, maxv=100):
    try:
        return max(0, min(100, float(v) / float(maxv) * 100))
    except (TypeError, ValueError, ZeroDivisionError):
        return 0
