import io
import os
import random
import string
import uuid

from PIL import Image
from dirtyfields import DirtyFieldsMixin
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class BaseModelWithUID(DirtyFieldsMixin, models.Model):
    class Meta:
        abstract = True

    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def get_slug_full_name(instance):
    name = f"{instance.first_name} {instance.last_name}"
    return name.strip()