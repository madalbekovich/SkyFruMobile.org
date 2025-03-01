from rest_framework import serializers



class GetOptimalFaresSerializer(serializers.Serializer):
    adult_count = serializers.IntegerField(help_text="Кл-во взрослых")
    child_count = serializers.IntegerField(default=0, help_text="Кл-во детей")
    infant_count = serializers.IntegerField(default=0, help_text="Кл-во младенцев")
    date_range = serializers.IntegerField(default=3, help_text="Диапазон дат")
    return_full_names = serializers.CharField(required=False)
    departure_point = serializers.CharField(required=True, help_text="Пункт отправления")
    arrival_point = serializers.CharField(required=True, help_text="Пункт прибытия")
    outbound_date = serializers.CharField(help_text="Дата отправления")
