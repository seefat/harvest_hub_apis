from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Q

from rest_framework import serializers
from rest_framework.exceptions import ValidationError, NotFound

from rest_framework.generics import get_object_or_404

from versatileimagefield.serializers import VersatileImageFieldSerializer

User = get_user_model()

class PrivateMeSerializer(serializers.ModelSerializer):
    image = VersatileImageFieldSerializer(
        required=False,
        sizes=[
            ("original", "url"),
            ("at256", "crop__256x256"),
            ("at512", "crop__512x512"),
        ],
    )
    

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "slug",
            "phone",
            "image",
            "email",
        ]

        read_only_fields = ["slug", "phone","username",]