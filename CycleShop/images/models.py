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

    bicycle = models.ForeignKey(
        'bicycles.Bicycle',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='bicycle_images'
    )

    accessory = models.ForeignKey(
        'accessories.Accessories',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='accessory_images',
    )

    components = models.ForeignKey(
        'components.Components',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='components_images',
    )

    equipment = models.ForeignKey(
        'equipment.Equipment',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='equipment_images',
    )

    def __str__(self):
        if self.bicycle:
            return f"{self.bicycle.name} Image"
        elif self.accessory:
            return f"{self.accessory.name} Image"
        elif self.components:
            return f"{self.components.name} Image"
        elif self.equipment:
            return f"{self.equipment.name} Image"
        else:
            return "Product Image"
