from django.utils.html import format_html
import django_tables2 as tables
from django_tables2.utils import A

from .models import GondoleRow


class GondoleRowTable(tables.Table):

    label = tables.LinkColumn(
        viewname='gondole:gondole-update', args=[A('pk')])

    def render_images(self, value):
        t = '<li class="row-display"><img src="{}" /></li>'
        shtml = ''
        for image in value.all():
            shtml += t.format(image.url)
        return format_html('<ul>%s</ul>' % shtml)

    class Meta:
        model = GondoleRow
        fields = ('position', 'label', 'images', 'active')
