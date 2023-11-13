from django.db import models

class ConnectionStatus(models.TextChoices):
    PENDING = 'PENDING', 'Pending'
    APPROVED = 'APPROVED', 'Approved'
    DECLINED = 'DECLINED', 'Declined'