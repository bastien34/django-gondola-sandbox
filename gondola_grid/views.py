from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'gondola_grid/homepage.html'


homepage = HomePageView.as_view()
