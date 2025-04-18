from rest_framework import serializers
from . import models


class FAQSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = '__all__'
    
class TechSupportFeedbackSerailizer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=13)
    class Meta:
        model = models.TechSupportFeedback
        fields = '__all__'

class NotificationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = '__all__'
    
    def get_formatted_date(self, obj):
        return obj.created_at.strftime('%d %B')