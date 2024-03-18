from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from CycleShop.images.models import ProductImage

MAX_CATEGORY_LENGTH = 50


class GogglesCategory(models.TextChoices):
    SUNGLASSES = "Sunglasses",
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
    MAX_SIZE_LENGTH = 10

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

    size = models.CharField(
        max_length=MAX_SIZE_LENGTH,
        choices=EquipmentSize.choices,
        null=False,
        blank=False,
    )

    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Goggles(Equipment):
    MAX_LENS_MATERIAL_LENGTH = 20
    MAX_FRAME_MATERIAL_LENGTH = 20

    UV_PROTECTION_LEVEL = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    LENS_MATERIAL = models.CharField(
        max_length=MAX_LENS_MATERIAL_LENGTH,
        null=True,
        blank=True,
    )

    FRAME_MATERIAL = models.CharField(
        max_length=MAX_LENS_MATERIAL_LENGTH,
        null=True,
        blank=True,
    )

    POLARIZED_LENSES = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    ANTI_FOG = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )
    
    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=GogglesCategory.choices,
    )


class Protection(Equipment):
    MAX_MATERIAL_LENGTH = 20
    MAX_WEIGHT = 5
    MAX_DECIMAL_PLACES = 3

    MATERIAL = models.CharField(
        max_length=MAX_MATERIAL_LENGTH,
        null=True,
        blank=True,
    )

    IMPACT_RESISTANCE_RATING = models.PositiveIntegerField(
        default=1,
        null=False,
        blank=False,
    )

    WEIGHT = models.DecimalField(
        max_digits=MAX_WEIGHT,
        decimal_places=MAX_DECIMAL_PLACES,
        null=False,
        blank=False,
    )

    ADJUSTABILITY = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    VENTILATION = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    WASHABLE = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=ProtectionCategory.choices,
    )


class Helmet(Equipment):
    MAX_CONSTRUCTION_TYPE_LENGTH = 15
    MAX_RETENTION_SYSTEM_LENGTH = 15
    MAX_SAFETY_CERTIFICATION_LENGTH = 10
    MAX_WEIGHT = 5
    MAX_DECIMAL_PLACES = 3

    CONSTRUCTION_TYPE = models.CharField(
        max_length=MAX_CONSTRUCTION_TYPE_LENGTH,
        null=False,
        blank=False,
    )

    RETENTION_SYSTEM = models.CharField(
        max_length=MAX_RETENTION_SYSTEM_LENGTH,
        null=True,
        blank=True,
    )

    SAFETY_CERTIFICATION = models.CharField(
        max_length=MAX_SAFETY_CERTIFICATION_LENGTH,
        null=True,
        blank=True,
    )

    WEIGHT = models.DecimalField(
        max_digits=MAX_WEIGHT,
        decimal_places=MAX_DECIMAL_PLACES,
        null=False,
        blank=False,
    )

    ADJUSTABLE_VISOR = models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    MIPS_TECHNOLOGY = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=HelmetCategory.choices,
    )


class Gloves(Equipment):
    MAX_MATERIAL_PALM_LENGTH = 10
    MAX_MATERIAL_BACK_LENGTH = 10
    MAX_PADDING_TYPE_LENGTH = 20
    MAX_GRIP_ENHANCING_FEATURES_LENGTH = 20
    MAX_CLOSURE_TYPE_LENGTH = 10

    MATERIAL_PALM = models.CharField(
        max_length=MAX_MATERIAL_PALM_LENGTH,
        null=True,
        blank=True,
    )

    MATERIAL_BACK = models.CharField(
        max_length=MAX_MATERIAL_PALM_LENGTH,
        null=True,
        blank=True,
    )

    PADDING_TYPE = models.CharField(
        max_length=MAX_PADDING_TYPE_LENGTH,
        null=True,
        blank=True,
    )

    GRIP_ENHANCING_FEATURES = models.CharField(
        max_length=MAX_GRIP_ENHANCING_FEATURES_LENGTH,
        null=True,
        blank=True,
    )

    CLOSURE_TYPE = models.CharField(
        max_length=MAX_CLOSURE_TYPE_LENGTH,
        null=True,
        blank=True,
    )

    WATERPROOF = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    TOUCHSCREEN_COMPATIBLE = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=GlovesCategory.choices,
    )

    images = GenericRelation(
        ProductImage,
        related_query_name="equipment",
    )
