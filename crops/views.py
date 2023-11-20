from rest_framework import generics
from .models import Category, BaseCrop, FarmerCrop
from .serializers import CategorySerializer, BaseCropSerializer, FarmerCropSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BaseCropListCreateView(generics.ListCreateAPIView):
    queryset = BaseCrop.objects.all()
    serializer_class = BaseCropSerializer

class BaseCropDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BaseCrop.objects.all()
    serializer_class = BaseCropSerializer

class FarmerCropListCreateView(generics.ListCreateAPIView):
    queryset = FarmerCrop.objects.all()
    serializer_class = FarmerCropSerializer

class FarmerCropDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarmerCrop.objects.all()
    serializer_class = FarmerCropSerializer
