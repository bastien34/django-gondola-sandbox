from django import template
from django.template.loader import get_template

from ..models import GondoleRow

register = template.Library()


@register.inclusion_tag('gondola_grid/gondola_grid.html')
def gondola():
    gondola_rows = GondoleRow.objects.filter(active=True)

    # t = get_template('gondola_grid/gondola_grid.html')
    context = {
        'gondola_rows': gondola_rows,
    }
    return context
