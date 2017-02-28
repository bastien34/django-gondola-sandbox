from django.forms import ModelForm
from .models import Gondola


class GondolaUpdateForm(ModelForm):

    class Meta:
        model = Gondola
        fields = ('label', 'description', 'link_to', 'position', 'image')