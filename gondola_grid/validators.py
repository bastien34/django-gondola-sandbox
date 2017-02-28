from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions


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
