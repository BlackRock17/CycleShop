from django.db import models

from CycleShop.core.validators import MaxFileSizeValidator

MAX_CATEGORY_LENGTH = 50


class GogglesCategory(models.TextChoices):
    SUNGLASSES = "sunglasses",
    SAFETY_GOGGLES = "Safety Goggles"


class ProtectionCategory(models.TextChoices):
    KNEE_PADS = "Knee Pads"
    ELBOW_PADS = "Elbow Pads"
    NECK_PROTECTORS = "Neck Protectors"
    BODY_PROTECTORS = "Body Protectors"
    SET_PROTECTORS = "Protectors Set"


class HelmetCategory(models.TextChoices):
    MOUNTAIN = "Mountain"
    MOUNTAIN_FULL_FACE = "Mountain Full Face"
    ROAD = "Road"
    URBAN = "Urban"


class GlovesCategory(models.TextChoices):
    LONG_FINGER = "Long Finger Gloves"
    SHORT_FINGER = "Short Finger Gloves"
    WINTER_GLOVES = "Winter Gloves"


class EquipmentSize(models.TextChoices):
    SIZE_S = "S"
    SIZE_M = "M"
    SIZE_L = "L"
    SIZE_XL = "XL"


class Equipment(models.Model):
    MAX_NAME_LENGTH = 50
    MAX_DIGITS = 8
    MAX_DECIMAL_PLACES = 2

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.DecimalField(
        max_digits=MAX_DIGITS,
        decimal_places=MAX_DECIMAL_PLACES,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name


class Goggles(Equipment):
    
    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=GogglesCategory.choices,
    )


class Protection(Equipment):

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=ProtectionCategory.choices,
    )


class Helmet(Equipment):

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=HelmetCategory.choices,
    )


class Gloves(Equipment):

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=GlovesCategory.choices,
    )


class EquipmentInventory(models.Model):
    MAX_SIZE_LENGTH = 10

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name="equipment_inventory",
    )

    size = models.CharField(
        max_length=MAX_SIZE_LENGTH,
        choices=EquipmentSize.choices,
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('equipment', 'size')

    def __str__(self):
        return f"{self.equipment.name} - Size: {self.size}, Quantity: {self.quantity}"


class EquipmentImage(models.Model):
    MAX_PHOTO_SIZE = 5 * 1024 * 1024

    image = models.ImageField(
        upload_to='equipment_images/',
        null=True,
        blank=True,
        validators=(MaxFileSizeValidator(limit_value=MAX_PHOTO_SIZE,),),
    )

    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='equipment_images'
    )