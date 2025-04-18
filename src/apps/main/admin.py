from django.contrib import admin
from . import models


@admin.register(models.TechSupportFeedback)
class TechSupportFeedbackAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(models.FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ["id", 'question']

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["id"]