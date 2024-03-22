from django.db import models
from CycleShop.core.validators import MaxFileSizeValidator


class ProductImage(models.Model):
    MAX_PHOTO_SIZE = 5 * 1024 * 1024

    image = models.ImageField(
        upload_to='product_images/',
        null=False,
        blank=False,
        validators=[MaxFileSizeValidator(limit_value=MAX_PHOTO_SIZE,)],
    )

    bicycle = models.ForeignKey('bicycles.Bicycle', on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.bicycle.name} Image"
