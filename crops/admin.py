from django.contrib import admin
from .models import Category, BaseCrop, FarmerCrop

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BaseCrop)
class BaseCropAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'variety')
    search_fields = ('name', 'variety')

@admin.register(FarmerCrop)
class FarmerCropAdmin(admin.ModelAdmin):
    list_display = ('crop', 'planting_date', 'harvest_date', 'farming_area', 'quantity', )
    search_fields = ('crop__name', 'planting_date', 'harvest_date')
