from rest_framework import serializers
from .models import Category, BaseCrop, FarmerCrop

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BaseCropSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCrop
        fields = '__all__'

class FarmerCropSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerCrop
        fields = '__all__'
