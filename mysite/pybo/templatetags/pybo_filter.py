from django import template

register = template.Library()


@register.filter # template filter
def sub(value, arg):
    return value - arg