from django.db import models
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


# validator
from django.template.loader import get_template


def validate_gondola(image):
    """
    Raise a validation error if the gondola image doesn't
    correspond on required size.

    Required sizes are:

        - 580 x 290
        - 380 x 380

    """

    allowed_sizes = (
        (580, 290),
        (380, 380),
    )

    img_size = get_image_dimensions(image)
    if img_size not in allowed_sizes:
        raise ValidationError('The image size is %s and should be one of %s'
                              % (img_size, allowed_sizes))

    return image


def validate_rectangle_gondola(image):
    """
    Raise a validation error if the gondola image is not a valid
    rectangle (580 x 290).
    :param image: image field
    :return: image
    """
    allowed_size = (580, 280)
    img_size = get_image_dimensions(image)
    if img_size not in allowed_size:
        raise ValidationError('Gondola image should be a rectangle %s instead'
                              'of %s' % (allowed_size, img_size))


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
    images = models.ManyToManyField(Gondola)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["active", "modified", "created"]
        verbose_name = "Gondola row"
        verbose_name_plural = "Gondola rows"

    def __str__(self):
        return self.label

    def save(self):
        """
        We limit the use of row to few combination of images. We rely on
        the number of gondole attached to the row and therefore on the total
        width.
        """

        # TODO: this validation

        allowed_width = 1160

        try:
            assert(self._get_total_width() == allowed_width)
        except AssertionError:
            raise AssertionError("You didn't fill all the image fields!")

        return super().save()

    def _get_total_width(self):
        return sum([i.width for i in self.images.all()])

    def as_html(self):
        t = get_template('gondola_grid/grid.html')
        context = {
            'gondole': self.images.all()
        }
        return t.render(context)



