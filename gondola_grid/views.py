from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView

from .models import GondoleRow
from .tables import GondoleRowTable


class GondolaDashboardView(ListView):
    """
    Dashboard view for Gondole management. This view should be
    password protected.
    """

    template_name = 'gondola_grid/dashboard/dashboard.html'
    model = GondoleRow

    def get_queryset(self):
        return self.model.objects.filter(active=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_gondole'] = GondoleRowTable(
            self.model.objects.filter(active=True))

        return context


dashboard_view = GondolaDashboardView.as_view()


class GondoleRowUpdateView(UpdateView):
    model = GondoleRow
    template_name = 'gondola_grid/dashboard/gondolerow_form.html'
    fields = ('label', 'active', 'position', 'images')


gondole_update_view = GondoleRowUpdateView.as_view()


class GondoleRowCreateView(CreateView):
    model = GondoleRow
    template_name = 'gondola_grid/dashboard/gondolerow_form.html'
    fields = ('label', 'active', 'position', 'images')


gondole_create_view = GondoleRowCreateView.as_view()
