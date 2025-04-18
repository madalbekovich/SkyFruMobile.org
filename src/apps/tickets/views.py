from django.shortcuts import render
from rest_framework import generics
from drf_spectacular.utils import extend_schema
from . import models, serializers

@extend_schema(summary="Получить Популярные направления",  tags=["Популярные направления"])
class PopularDestinationView(generics.ListAPIView):
    queryset = models.PopularDestination.objects.all()
    serializer_class = serializers.PopularDestinationSerializer