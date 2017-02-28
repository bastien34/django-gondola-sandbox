from django.conf.urls import url
from .views import dashboard_view


urlpatterns = [
    url(r'^dashboard', dashboard_view, name='dashboard'),
]
