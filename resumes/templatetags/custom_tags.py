from django import template

register = template.Library()


@register.filter
def skill_percents(value):
    try:
        return (int(value) / 5) * 100
    except (ValueError, ZeroDivisionError):
        return 0
