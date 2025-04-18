from rest_framework import serializers



class GetOptimalFaresSerializer(serializers.Serializer):
    adult_count = serializers.IntegerField(help_text="Кл-во взрослых")
    child_count = serializers.IntegerField(default=0, help_text="Кл-во детей")
    infant_count = serializers.IntegerField(default=0, help_text="Кл-во младенцев")
    date_range = serializers.IntegerField(default=3, help_text="Диапазон дат", min_value=1, max_value=3)
    # return_full_names = serializers.CharField(required=False)
    owrt = serializers.ChoiceField(help_text='Тип перелета', choices=[("OW"), ("RT")])
    departure_point = serializers.CharField(required=True, help_text="Пункт отправления")
    arrival_point = serializers.CharField(required=True, help_text="Пункт прибытия")
    # max_count = serializers.IntegerField(help_text="Максимальное количество предложений")
    outbound_date = serializers.CharField(help_text="Дата отправления")
    return_date = serializers.CharField(help_text="Дата возвр", required=False)
    