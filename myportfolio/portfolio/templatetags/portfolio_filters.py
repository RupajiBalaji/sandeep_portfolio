from django import template

register = template.Library()


@register.filter
def split(value, arg):
    """Split a string by the given separator"""
    if value:
        return value.split(arg)
    return []


@register.filter
def mul(value, arg):
    """Multiply value by arg"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def strip(value):
    """Strip whitespace from string"""
    if isinstance(value, str):
        return value.strip()
    return value
