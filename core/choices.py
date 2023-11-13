from django.db import models


class UserType(models.TextChoices):
    FARMER = "FARMER", "Farmer"
    DOCTOR = "DOCTOR", "Doctor"

class UserStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PLACEHOLDER = "PLACEHOLDER", "Placeholder"
    ACTIVE = "ACTIVE", "Active"
    HIDDEN = "HIDDEN", "Hidden"
    PAUSED = "PAUSED", "Paused"
    REMOVED = "REMOVED", "Removed"
