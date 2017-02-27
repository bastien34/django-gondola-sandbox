from .models import GondoleRow, Gondola
from django.contrib import admin


class GondoleRowAdmin(admin.ModelAdmin):
    fields = ['label', 'images', ('position', 'active')]
    filter_horizontal = ('images',)
    list_display = ('label', 'created', 'active',)


class GondolaAdmin(admin.ModelAdmin):
    fields = ['link_to', 'image', 'label', 'description', 'position']


admin.site.register(GondoleRow, GondoleRowAdmin)
admin.site.register(Gondola, GondolaAdmin)
