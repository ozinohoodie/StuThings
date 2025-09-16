from django import template
register = template.Library()

@register.filter
def pluralize_copy(n: int) -> str:
    return "copy" if n == 1 else "copies"