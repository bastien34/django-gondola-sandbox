from django import template

from ..models import GondoleRow

register = template.Library()


@register.inclusion_tag('gondola_grid/gondola_grid.html')
def gondola():
    gondola_rows = GondoleRow.objects.filter(active=True)

    context = {
        'gondola_rows': gondola_rows,
    }
    return context
