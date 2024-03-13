from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from CycleShop.core.validators import MaxFileSizeValidator


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


class BicycleSizeChoices(models.TextChoices):
    SIZE_S = "S"
    SIZE_M = "M"
    SIZE_L = "L"
    SIZE_XL = "XL"


class TyreSize(models.TextChoices):
    SIZE_TWENTY_SIX = "26"
    SIZE_TWENTY_SEVEN = "27.5"
    SIZE_TWENTY_NINE = "29"


class BicycleInventoryManager(models.Manager):
    def create(self, *args, **kwargs):
        content_object = kwargs.get('content_object')
        quantity = kwargs.get('quantity')
        if self.filter(content_object=content_object, quantity=quantity).exists():
            raise ValueError('Inventory record with the same bike and quantity already exists.')
        return super().create(*args, **kwargs)


class Bicycle(models.Model):
    MAX_NAME_LENGTH = 100
    MAX_FRAME_LENGTH = 100
    MAX_FORK_LENGTH = 100
    MAX_BRAKES_LENGTH = 100
    MAX_SPEEDS_LENGTH = 100
    MAX_TIRES_LENGTH = 100
    MAX_COLOR_LENGTH = 20

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

    tires = models.CharField(
        max_length=MAX_TIRES_LENGTH,
        null=False,
        blank=False,
    )

    fork_travel = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    frame_travel = models.PositiveIntegerField(
        null=True,
        blank=True,
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

    class Meta:
        abstract = True


class MountainBicycle(Bicycle):
    MAX_CATEGORY_LENGTH = 30
    MAX_SIZE_LENGTH = 10
    MAX_TYRES_SIZE_LENGTH = 10

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        choices=MountainBicycleCategory.choices,
        null=False,
        blank=False,
    )

    tyres_size = models.CharField(
        max_length=MAX_TYRES_SIZE_LENGTH,
        choices=TyreSize.choices,
        null=False,
        blank=False,
    )


class RoadBicycle(Bicycle):
    MAX_CATEGORY_LENGTH = 30
    MAX_SIZE_LENGTH = 10

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
    MAX_TYRES_SIZE_LENGTH = 10

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        choices=ElectricBicycleCategory.choices,
        null=False,
        blank=False,
    )

    tyres_size = models.CharField(
        max_length=MAX_TYRES_SIZE_LENGTH,
        choices=TyreSize.choices,
        null=False,
        blank=False,
    )

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


class BicycleSize(models.Model):
    MAX_SIZE_LENGTH = 10

    size = models.CharField(
        max_length=MAX_SIZE_LENGTH,
        choices=BicycleSizeChoices.choices,
    )

    def __str__(self):
        return self.size


class BicycleInventory(models.Model):
    DEFAULT_QUANTITY = 0

    quantity = models.PositiveIntegerField(
        default=DEFAULT_QUANTITY,
    )

    sizes = models.ManyToManyField(
        BicycleSize,
        blank=True
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )

    objects = BicycleInventoryManager()


class BicycleImage(models.Model):
    MAX_PHOTO_SIZE = 5 * 1024 * 1024

    image = models.ImageField(
        upload_to='bicycle_images/',
        null=False,
        blank=False,
        validators=(MaxFileSizeValidator(limit_value=MAX_PHOTO_SIZE, ),),
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE
    )

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey(
        'content_type',
        'object_id'
    )
