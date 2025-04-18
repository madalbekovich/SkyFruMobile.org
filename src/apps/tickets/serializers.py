from rest_framework import serializers
from . import models

class PopularDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PopularDestination
        fields = '__all__'