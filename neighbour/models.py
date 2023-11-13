from django.db import models
from django.contrib.auth import get_user_model

from autoslug import AutoSlugField

from core.utils import BaseModelWithUID

from .choices import ConnectionStatus
# Create your models here.

def get_slug(instance):
    return (f"{instance.current_user.username} connected {instance.connected_user.username}").strip()

User = get_user_model()


class UserConnection(BaseModelWithUID, models.Model):
    current_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='current_user_connections')
    connected_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='connected_user_connections')
    connection_status = models.CharField(max_length=20, choices=ConnectionStatus.choices,default=ConnectionStatus.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from =get_slug , max_length=50, unique=True, blank=True)