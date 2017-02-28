#  noqa

from django.conf.urls import url
from .views import (dashboard_view, gondole_update_view, gondole_create_view,
                    gondole_list_view, gondole_delete_view,
                    gondola_create_view, gondola_delete_view,
                    gondola_update_view, )


urlpatterns = [
    url(r'^dashboard$', dashboard_view, name='dashboard'),
    url(r'^gondole-list$', gondole_list_view, name='gondole-list'),

    # Gondole row editing
    url(r'^gondole-create$', gondole_create_view, name='gondole-create'),
    url(r'^gondole-update-(?P<pk>\d+)$', gondole_update_view, name='gondole-update'),
    url(r'^gondole-delete-(?P<pk>\d+)$', gondole_delete_view, name='gondole-delete'),

    # Gondola editing
    url(r'^gondola-create$', gondola_create_view, name='gondola-create'),
    url(r'^gondola-update-(?P<pk>\d+)$', gondola_update_view, name='gondola-update'),
    url(r'^gondola-delete-(?P<pk>\d+)$', gondola_delete_view, name='gondola-delete'),
]
