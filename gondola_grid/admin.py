from django.contrib import admin
from .models import GondoleRow, Gondola
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.contrib import admin

from django.utils.html import format_html


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(format_html(u'<a href="%s" target="_blank"><img src="%s" alt="%s" /></a> %s ' % \
                          (image_url, image_url, file_name, _('Change:'))))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ImageWidgetAdmin(admin.ModelAdmin):
    image_fields = []

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in self.image_fields:
            request = kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageWidgetAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class GondoleRowAdmin(admin.ModelAdmin):
    fields = ['label', 'images', ('position', 'active')]
    filter_horizontal = ('images',)
    list_display = ('label', 'created', 'active',)


class GondolaAdmin(admin.ModelAdmin):
    fields = ['link_to', 'image', 'label', 'description', 'position']


admin.site.register(GondoleRow, GondoleRowAdmin)
admin.site.register(Gondola, GondolaAdmin)
