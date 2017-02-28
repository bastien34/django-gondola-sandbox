from django.views.generic.base import TemplateView


class GondolaDashboardView(TemplateView):
    """
    Dashboard view for Gondole management. This view should be
    password protected.
    """
    template_name = 'gondola_grid/dashboard.html'

dashboard_view = GondolaDashboardView.as_view()