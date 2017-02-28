from django.views.generic.list import ListView
from .models import GondoleRow


class GondolaDashboardView(ListView):
    """
    Dashboard view for Gondole management. This view should be
    password protected.
    """

    template_name = 'gondola_grid/dashboard.html'
    model = GondoleRow

    def get_queryset(self):
        return self.model.objects.filter(active=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_gondole'] = self.model.objects.filter(active=True)
        return context


dashboard_view = GondolaDashboardView.as_view()
