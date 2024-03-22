from django.core.validators import MinLengthValidator
from django.db import models

from CycleShop.images.models import ProductImage


class Category(models.TextChoices):
    BIKE_CARRIERS = "Bike Carriers"
    BIKE_RACKS = "Bike Racks"
    CHILD_BIKE_SEAD = "Child Bike Seat"
    PANNIERS_AND_BAGS = "Panniers and Bags"
    BELLS_AND_HORNS = "Bells and Horns"
    MUDGUARDS = "Mudguards"
    LOCKS = "Locks"
    BASKETS = "Baskets"
    MIRRORS = "Mirrors"
    PUMPS = "Pumps"
    FOOTPEGS = "Footpegs"
    PHONE_HOLDER = "Phone Holder"
    FRAME_AND_SADDLE_GABS = "Frame and Saddle Bags"


class Accessories(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_TYPE_LENGTH = 30
    MIN_DESCRIPTION_LENGTH = 10

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
        validators=[MinLengthValidator(MIN_DESCRIPTION_LENGTH)]
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=30,
        choices=Category.choices
    )


