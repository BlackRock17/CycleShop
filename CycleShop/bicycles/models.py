from django.db import models


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

    bicycle = models.ForeignKey(
        Bicycle,
        on_delete=models.CASCADE,
        related_name='inventory'
    )

    sizes = models.ManyToManyField(
        BicycleSize,
        blank=True
    )

    class Meta:
        unique_together = ['bicycle', 'quantity']
