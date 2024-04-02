from django.core.validators import MinLengthValidator
from django.db import models

from CycleShop.images.models import ProductImage


class ComponentsType(models.TextChoices):
    CASSETTES = ("Cassettes", "Cassettes")
    CHAINS = ("Chains", "Chains")
    FORKS = ("Forks", "Forks")
    TUBELESS_TYRES = ("Tubeless Tyres", "Tubeless Tyres")
    INNER_TUBES = ("Inner Tubes", "Inner Tubes")
    HUBS = ("Hubs", "Hubs")
    REAR_SHOCK_ABSORBERS = ("Rear Shock Absorbers", "Rear Shock Absorbers")
    REAR_DERAILLEURS = ("Rear Derailleurs", "Rear Derailleurs")
    SPOKES = ("Spokes", "Spokes")
    SEATPOST_CLAMPS = ("Seatpost Clamps", "Seatpost Clamps")
    SHIFTERS = ("Shifters", "Shifters")
    HANDLEBARS = ("Handlebars", "Handlebars")
    CRANKS = ("Cranks", "Cranks")
    PEDALS = ("Pedals", "Pedals")
    FRONT_DERAILLEUR = ("Front Derailleur", "Front Derailleur")
    SADDLES = ("Saddles", "Saddles")
    BRAKES = ("Brakes", "Brakes")


class Components(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_TYPE_LENGTH = 30
    MIN_DESCRIPTION_LENGTH = 10
    MAX_INSTALATION_TYPE_LENGTH = 15
    MAX_SPEED_COMPATIBILITY_LENGTH = 15

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

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=False,
        blank=False,
        default=0.00
    )

    installation_type = models.CharField(
        max_length=MAX_INSTALATION_TYPE_LENGTH,
        null=True,
        blank=True,
    )

    speed_compatibility = models.CharField(
        max_length=MAX_SPEED_COMPATIBILITY_LENGTH,
        null=True,
        blank=True,
    )
