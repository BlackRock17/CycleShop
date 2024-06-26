from django.db import models
from CycleShop.images.models import ProductImage

MAX_CATEGORY_LENGTH = 50


class GogglesCategory(models.TextChoices):
    SUNGLASSES = ("Sunglasses", "Sunglasses")
    SAFETY_GOGGLES = ("Safety Goggles", "Safety Goggles")


class ProtectionCategory(models.TextChoices):
    KNEE_PADS = ("Knee Pads", "Knee Pads")
    ELBOW_PADS = ("Elbow Pads", "Elbow Pads")
    NECK_PROTECTORS = ("Neck Protectors", "Neck Protectors")
    BODY_PROTECTORS = ("Body Protectors", "Body Protectors")
    SET_PROTECTORS = ("Protectors Set", "Protectors Set")


class HelmetCategory(models.TextChoices):
    MOUNTAIN = ("Mountain", "Mountain")
    MOUNTAIN_FULL_FACE = ("Mountain Full Face", "Mountain Full Face")
    ROAD = ("Road", "Road")
    URBAN = ("Urban", "Urban")


class GlovesCategory(models.TextChoices):
    LONG_FINGER = ("Long Finger Gloves", "Long Finger Gloves")
    SHORT_FINGER = ("Short Finger Gloves", "Short Finger Gloves")
    WINTER_GLOVES = ("Winter Gloves", "Winter Gloves")


class EquipmentSize(models.TextChoices):
    SIZE_S = ("S", "S")
    SIZE_M = ("M", "M")
    SIZE_L = ("L", "L")
    SIZE_XL = ("XL", "XL")


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

    @staticmethod
    def get_category_choices(equipment_type):
        if equipment_type == "Goggles":
            return GogglesCategory.choices
        elif equipment_type == "Protection":
            return ProtectionCategory.choices
        elif equipment_type == "Helmet":
            return HelmetCategory.choices
        elif equipment_type == "Gloves":
            return GlovesCategory.choices
        else:
            return []


class Goggles(Equipment):
    MAX_LENS_MATERIAL_LENGTH = 40
    MAX_FRAME_MATERIAL_LENGTH = 40

    UV_protection_level = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    lens_material = models.CharField(
        max_length=MAX_LENS_MATERIAL_LENGTH,
        null=True,
        blank=True,
    )

    frame_material = models.CharField(
        max_length=MAX_LENS_MATERIAL_LENGTH,
        null=True,
        blank=True,
    )

    polarized_lenses = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    anti_fog = models.BooleanField(
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
    MAX_MATERIAL_LENGTH = 30
    MAX_WEIGHT = 5
    MAX_DECIMAL_PLACES = 3

    material = models.CharField(
        max_length=MAX_MATERIAL_LENGTH,
        null=True,
        blank=True,
    )

    impact_resistance_rating = models.PositiveIntegerField(
        default=1,
        null=False,
        blank=False,
    )

    weight = models.DecimalField(
        max_digits=MAX_WEIGHT,
        decimal_places=MAX_DECIMAL_PLACES,
        null=False,
        blank=False,
    )

    adjustability = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    ventilation = models.BooleanField(
        default=True,
        null=False,
        blank=False,
    )

    washable = models.BooleanField(
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
    MAX_CONSTRUCTION_TYPE_LENGTH = 30
    MAX_RETENTION_SYSTEM_LENGTH = 30
    MAX_SAFETY_CERTIFICATION_LENGTH = 30
    MAX_WEIGHT = 5
    MAX_DECIMAL_PLACES = 3

    construction_type = models.CharField(
        max_length=MAX_CONSTRUCTION_TYPE_LENGTH,
        null=False,
        blank=False,
    )

    retention_system = models.CharField(
        max_length=MAX_RETENTION_SYSTEM_LENGTH,
        null=True,
        blank=True,
    )

    safety_certification = models.CharField(
        max_length=MAX_SAFETY_CERTIFICATION_LENGTH,
        null=True,
        blank=True,
    )

    weight = models.DecimalField(
        max_digits=MAX_WEIGHT,
        decimal_places=MAX_DECIMAL_PLACES,
        null=False,
        blank=False,
    )

    adjustable_visor = models.BooleanField(
        default=False,
        blank=False,
        null=False,
    )

    MIPS_technology = models.BooleanField(
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
    MAX_MATERIAL_PALM_LENGTH = 30
    MAX_MATERIAL_BACK_LENGTH = 30
    MAX_PADDING_TYPE_LENGTH = 30
    MAX_GRIP_ENHANCING_FEATURES_LENGTH = 30
    MAX_CLOSURE_TYPE_LENGTH = 30

    material_palm = models.CharField(
        max_length=MAX_MATERIAL_PALM_LENGTH,
        null=True,
        blank=True,
    )

    material_back = models.CharField(
        max_length=MAX_MATERIAL_PALM_LENGTH,
        null=True,
        blank=True,
    )

    padding_type = models.CharField(
        max_length=MAX_PADDING_TYPE_LENGTH,
        null=True,
        blank=True,
    )

    grip_enhancing_features = models.CharField(
        max_length=MAX_GRIP_ENHANCING_FEATURES_LENGTH,
        null=True,
        blank=True,
    )

    closure_type = models.CharField(
        max_length=MAX_CLOSURE_TYPE_LENGTH,
        null=True,
        blank=True,
    )

    waterproof = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    touchscreen_compatible = models.BooleanField(
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

