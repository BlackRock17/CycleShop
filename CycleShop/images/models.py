from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from CycleShop.core.validators import MaxFileSizeValidator


class ProductImage(models.Model):
    MAX_PHOTO_SIZE = 5 * 1024 * 1024

    image = models.ImageField(
        upload_to='product_images/',
        null=False,
        blank=False,
        validators=[MaxFileSizeValidator(limit_value=MAX_PHOTO_SIZE,)],
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
