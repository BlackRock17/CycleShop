from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models
from CycleShop.accounts.managers import CycleShopUserManager


class CycleShopUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    objects = CycleShopUserManager()

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    USERNAME_FIELD = "username"


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 25
    MAX_LAST_NAME_LENGTH = 25
    MAX_TOWN_LENGTH = 25
    MAX_ADDRESS_LENGTH = 100
    MAX_POSTCODE_LENGTH = 10

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    town = models.CharField(
        max_length=MAX_TOWN_LENGTH,
        null=False,
        blank=False,
    )

    address = models.CharField(
        max_length=MAX_ADDRESS_LENGTH,
        null=False,
        blank=False,
    )

    postcode = models.CharField(
        max_length=MAX_POSTCODE_LENGTH,
        null=False,
        blank=False,
    )

    user = models.OneToOneField(
        CycleShopUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )