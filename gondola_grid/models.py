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
    image = models.ImageField(validators=[validate_gondola])
    link_to = models.URLField(blank=True, null=True)
    label = models.CharField(max_length=256)
    description = models.CharField(max_length=256, blank=True, null=True)

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
    label = models.CharField(max_length=250, default='Gondole row')
    position = models.SmallIntegerField(default=1)
    image_1 = models.ForeignKey(Gondola, related_name='first_image')
    image_2 = models.ForeignKey(Gondola, related_name='second_image')
    image_3 = models.ForeignKey(Gondola, related_name='third_image',
                                blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ["active", "modified", "created"]
        verbose_name = "Gondola row"
        verbose_name_plural = "Gondola rows"

    def image1_tag(self):
        return u'<img src="%s" />' % self.image_1.url
    image1_tag.short_description = 'Image'
    image1_tag.allow_tags = True

    def image2_tag(self):
        return u'<img src="%s" />' % self.image_2.url
    image2_tag.short_description = 'Image'
    image2_tag.allow_tags = True

    def image3_tag(self):
        return u'<img src="%s" />' % self.image_3.url
    image3_tag.short_description = 'Image'
    image3_tag.allow_tags = True

    def save(self):
        width = 0
        allowed_width = 1160

        if self.image_3:
            allowed_width = 1340

        width = sum([i.width for i in self.images])

        try:
            assert(width == allowed_width)
        except AssertionError:
            raise AssertionError("You didn't fill all the image fields!")

        return super().save()

    @property
    def images(self):
        images = [self.image_1, self.image_2]
        if self.image_3:
            images.append(self.image_3)
        return images

    def as_html(self):
        t = get_template('gondola_grid/grid.html')
        context = {
            'gondole': self.images
        }
        return t.render(context)



