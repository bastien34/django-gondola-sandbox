from django.conf.urls import url
from .views import dashboard_view, gondole_update_view, gondole_create_view


urlpatterns = [
    url(r'^dashboard$', dashboard_view, name='dashboard'),
    url(r'^gondole-update-(?P<pk>\d+)', gondole_update_view,
        name='gondole-update'),
    url(r'^gondole-create$', gondole_create_view, name='gondole-create'),
]
