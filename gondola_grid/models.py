from django.db import models
from django.template.loader import get_template
from django.urls.base import reverse

from .validators import validate_gondola


class Gondola(models.Model):
    """
    Gondola is an image profiled to be displayed in a gondole grid.
    It aims to highlight a feature, a product range or whatever.
    """
    label = models.CharField(max_length=256)
    image = models.ImageField(validators=[validate_gondola])
    link_to = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=256, blank=True, null=True)
    position = models.SmallIntegerField(default=1)

    class Meta:
        ordering = ['position', ]
        verbose_name_plural = 'gondole'

    def __str__(self):
        return 'Gondola %s: %s' % (self.type, self.label)

    @property
    def type(self):
        if self.image.width == self.image.height:
            return 'square'
        return 'rectangle'

    @property
    def height(self):
        return self.image.height

    @property
    def width(self):
        return self.image.width

    @property
    def url(self):
        return self.image.url


class GondoleRow(models.Model):
    """
    Row of gondole. Aims.

                ———————————————————————
                |  A  |    B    |     |
                ————————————————|  E  |
                |    C    |  D  |     |
                ——————————————————————|
                |          F          |
                ———————————————————————

    """

    active = models.BooleanField(default=True)
    label = models.CharField(max_length=250, default='Gondola row')
    position = models.SmallIntegerField(default=1)
    images = models.ManyToManyField(
        Gondola,
        help_text="Select at least 2 rectangles or 1 rectangle and 2 squares.")

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["active", 'position', "modified", "created"]
        verbose_name = "Gondole row"
        verbose_name_plural = "Gondole rows"

    def __str__(self):
        return self.label

    # def save(self, *args, **kwargs):
    #     """
    #     We limit the use of row to few combination of images. We rely on
    #     the number of gondole attached to the row and therefore on the total
    #     width.
    #     """
    #
    #     # TODO: this validation
    #
    #     allowed_width = 1160
    #
    #     try:
    #         assert(self._get_total_width() == allowed_width)
    #     except AssertionError:
    #         raise AssertionError("You didn't fill all the image fields!")
    #
    #     super().save(*args, **kwargs)

    def _get_total_width(self):
        return sum([i.width for i in self.images.all()])

    def as_html(self):
        t = get_template('gondola_grid/gondola_row.html')
        context = {
            'gondole': self.images.all()
        }
        return t.render(context)

    def get_absolute_url(self):
        # return reverse('dashboard', kwargs={'pk': self.pk})
        return reverse('gondole:dashboard')
