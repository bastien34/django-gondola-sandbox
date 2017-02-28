from django.template.loader import get_template
import django_tables2 as tables

from .models import GondoleRow


class GondoleRowTable(tables.Table):

    def render_images(self, value):
        t = get_template('gondola_grid/dashboard/_gondola_cell_table.html')
        return t.render({'images': value.all(), 'row': value.instance, })

    class Meta:
        model = GondoleRow
        fields = ('position', 'images', 'active')
