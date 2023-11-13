from django.db import models
from django.contrib.auth import get_user_model

from core.utils import BaseModelWithUID


User = get_user_model()


class Category(BaseModelWithUID, models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BaseCrop(BaseModelWithUID, models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    variety = models.CharField(
        max_length=100, blank=True, help_text="Crop variety, if applicable"
    )

    def __str__(self):
        return self.name


class FarmerCrop(BaseModelWithUID, models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    crop = models.ForeignKey(BaseCrop, on_delete=models.CASCADE)
    planting_date = models.DateField()
    harvest_date = models.DateField(help_text="Expected harvest date")
    farming_area = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(
        help_text="Quantity of the crop in kilograms"
    )

    class Meta:
        unique_together = ["crop", "planting_date"]

    def __str__(self):
        return f"{self.crop.name} - {self.harvest_date.year} Details"
