import os
import shutil

from django.core.management.base import CommandError
from django.views.generic.base import TemplateView
from django.core.management import call_command


class HomePageView(TemplateView):
    template_name = 'demo/homepage.html'

    def get(self, request, *args, **kwargs):
        if 'init' in request.GET:

            # import fixtures
            try:
                call_command('loaddata', 'fixtures/gondole.json')
            except CommandError:
                raise CommandError("Bouh, don't know what's wrong here")

            # copy files
            src = 'static/img/'
            dst = 'media'
            files = os.listdir(src)
            for f in files:
                shutil.copy(os.path.join('static/img', f), dst)

        return super().get(request, *args, **kwargs)


homepage = HomePageView.as_view()
