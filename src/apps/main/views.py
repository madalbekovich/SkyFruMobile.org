# rest framework
from rest_framework import generics

# packages
from drf_spectacular.utils import extend_schema



# your import 
from . import models
from . import serializers


@extend_schema(summary="Получить список FAQ",  tags=["FAQ"])
class FAQView(generics.ListAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerailizer

@extend_schema(summary="Получить список Уведомлений",  tags=["Уведомления"])
class NotificationListView(generics.ListAPIView):
    queryset = models.Notification.objects.all()
    serializer_class = serializers.NotificationSerailizer

@extend_schema(summary="Написать ТЕХ.Поддержку",  tags=["Обратная связь"])
class TechSupportFeedbackView(generics.CreateAPIView):
    queryset = models.TechSupportFeedback.objects.all()
    serializer_class = serializers.TechSupportFeedbackSerailizer