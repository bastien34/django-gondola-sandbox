"""

Gondola URL Configuration

"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from demo.views import homepage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', homepage, name='index'),
    url(r'^gondola/', include('gondola.urls', namespace='gondola')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT}),
    ]
