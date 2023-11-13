import logging

from rest_framework.generics import RetrieveUpdateAPIView, get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.rest.serializers.me import PrivateMeSerializer


class PrivateMeDetail(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PrivateMeSerializer

    def get_object(self):
        return self.request.user