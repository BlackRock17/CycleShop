from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from CycleShop.images.models import ProductImage


class MountainBicycleCategory(models.TextChoices):
    HARD_TRAIL = "Hard Trail"
    FULL_SUSPENSION = "Full Suspension"
    FAT_BIKE = "Fat Bike"


class RoadBicycleCategory(models.TextChoices):
    GRAVEL_BIKES = "Gravel"
    CYCLOCROSS_BIKES = "Cyclocross"
    FIXIE = "Fixie"
    TRIATHLON = "Triathlon"


class ElectricBicycleCategory(models.TextChoices):
    ELECTRIC_MOUNTAIN = "Electric mountain"
    ELECTRIC_CITY = "Electric city"
    ELECTRIC_KIDS = "Electric kids"
    ELECTRIC_ROAD = "Electric road"


class BicycleSize(models.TextChoices):
    SIZE_S = "S"
    SIZE_M = "M"
    SIZE_L = "L"
    SIZE_XL = "XL"


class TyreSize(models.TextChoices):
    SIZE_TWENTY_SIX = "26"
    SIZE_TWENTY_SEVEN = "27.5"
    SIZE_TWENTY_NINE = "29"


class HandlebarType(models.TextChoices):
    DROP = "Drop"
    BULLHORN = "Bullhorn"
    FLAT = "Flat"


class Bicycle(models.Model):
    MAX_NAME_LENGTH = 100
    MAX_FRAME_LENGTH = 100
    MAX_FORK_LENGTH = 100
    MAX_BRAKES_LENGTH = 100
    MAX_SPEEDS_LENGTH = 100
    MAX_TIRES_LENGTH = 100
    MAX_COLOR_LENGTH = 20
    MAX_TYRES_SIZE_LENGTH = 10
    MAX_SIZE_LENGTH = 10

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField()

    frame = models.CharField(
        max_length=MAX_FRAME_LENGTH,
        null=False,
        blank=False,
    )

    fork = models.CharField(
        max_length=MAX_FORK_LENGTH,
        null=True,
        blank=True,
    )

    brakes = models.CharField(
        max_length=MAX_BRAKES_LENGTH,
        null=False,
        blank=False,
    )

    gears = models.CharField(
        max_length=MAX_SPEEDS_LENGTH,
        null=True,
        blank=True,
    )

    tyres_size = models.CharField(
        max_length=MAX_TYRES_SIZE_LENGTH,
        choices=TyreSize.choices,
        null=False,
        blank=False,
    )

    weight = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )

    color = models.CharField(
        max_length=MAX_COLOR_LENGTH,
        null=True,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )

    size = models.CharField(
        max_length=MAX_SIZE_LENGTH,
        choices=BicycleSize.choices,
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField()

    images = GenericRelation(
        ProductImage,
        related_query_name="bicycle"
    )

    def __str__(self):
        return self.name


class MountainBicycle(Bicycle):
    MAX_CATEGORY_LENGTH = 30
    MAX_SIZE_LENGTH = 10

    fork_travel = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    frame_travel = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    suspension_lockout = models.BooleanField(
        default=True,
    )

    dropper_post = models.BooleanField(
        default=True,
    )

    tubeless_ready = models.BooleanField(
        default=False,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        choices=MountainBicycleCategory.choices,
        null=False,
        blank=False,
    )


class RoadBicycle(Bicycle):
    MAX_CATEGORY_LENGTH = 30
    MAX_SIZE_LENGTH = 10
    MAX_HANDLEBAR_TYPE_LENGTH = 10
    MAX_FRAME_GEOMETRY_LENGTH = 10

    handlebar_type = models.CharField(
        max_length=MAX_HANDLEBAR_TYPE_LENGTH,
        null=False,
        blank=False,
        choices=HandlebarType.choices,
    )

    frame_geometry = models.CharField(
        max_length=MAX_FRAME_GEOMETRY_LENGTH,
        null=True,
        blank=True,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        choices=RoadBicycleCategory.choices,
        null=False,
        blank=False,
    )


class ElectricBicycle(Bicycle):
    MAX_CATEGORY_LENGTH = 30
    MAX_ENGINE_LENGTH = 50
    MAX_BATTERY_LENGTH = 50
    MAX_DISPLAY_LENGTH = 50
    MAX_CHARGER_LENGTH = 50
    MAX_SIZE_LENGTH = 10

    engine = models.CharField(
        max_length=MAX_ENGINE_LENGTH,
        null=False,
        blank=False,
    )

    battery = models.CharField(
        max_length=MAX_BATTERY_LENGTH,
        null=False,
        blank=False,
    )

    display = models.CharField(
        max_length=MAX_DISPLAY_LENGTH,
        null=False,
        blank=False,
    )

    charger = models.CharField(
        max_length=MAX_CHARGER_LENGTH,
        null=False,
        blank=False,
    )

    motor_power = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    max_speed = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        choices=ElectricBicycleCategory.choices,
        null=False,
        blank=False,
    )


