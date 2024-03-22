from django.contrib.contenttypes.fields import GenericRelation
from django.core.validators import MinLengthValidator
from django.db import models

from CycleShop.images.models import ProductImage


class ComponentsType(models.TextChoices):
    CASSETTES = "Cassettes"
    CHAINS = "Chains"
    FORKS = "Forks"
    TUBELESS_TYRES = "Tubeless Tyres"
    INNER_TUBES = "Inner Tubes"
    HUBS = "Hubs"
    REAR_SHOCK_ABSORBERS = "Rear Shock Absorbers"
    REAR_DERAILLEURS = "Rear Derailleurs"
    SPOKES = "Spokes"
    SEATPOST_CLAMPS = "Seatpost Clamps"
    SHIFTERS = "Shifters"
    HANDLEBARS = "Handlebars"
    CRANKS = "Cranks"
    PEDALS = "Pedals"
    FRONT_DERAILLEUR = "Front Derailleur"
    SADDLES = "Saddles"
    BRAKES = "Brakes"


class Components(models.Model):
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

    type = models.CharField(
        max_length=MAX_TYPE_LENGTH,
        null=False,
        blank=False,
        choices=ComponentsType.choices,
    )

    quantity = models.PositiveIntegerField()
