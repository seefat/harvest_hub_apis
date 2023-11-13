from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from autoslug import AutoSlugField

from phonenumber_field.modelfields import PhoneNumberField
from simple_history.models import HistoricalRecords

from versatileimagefield.fields import VersatileImageField, PPOIField

from .choices import UserType, UserStatus
from .managers import CustomUserManager
from .utils import BaseModelWithUID, get_slug_full_name


class User(AbstractBaseUser, PermissionsMixin, BaseModelWithUID):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    username = models.CharField(max_length=50, unique=True, db_index=True)
    slug = AutoSlugField(populate_from=get_slug_full_name, editable=False, unique=True)
    phone = PhoneNumberField(blank=True, unique=True, db_index=True)
    email = models.EmailField(blank=True)
    image = VersatileImageField(
        width_field="width",
        height_field="height",
        ppoi_field="ppoi",
        null=True,
        blank=True,
    )
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        db_index=True,
        default=UserType.FARMER,
    )
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        db_index=True,
        default=UserStatus.ACTIVE,
    )
    is_active = models.BooleanField(default=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    ppoi = PPOIField()

    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=True)

    REQUIRED_FIELDS = (
        "first_name",
        "last_name",
        "phone",
    )
    USERNAME_FIELD = "username"

    # Managers
    objects = CustomUserManager()

    # History
    history = HistoricalRecords()

    def __str__(self):
        name = " ".join([self.first_name, self.last_name])
        return f"Phone: {str(self.phone)}, Name: {name}"
