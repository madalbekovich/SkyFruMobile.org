from django.contrib import admin
from .models import PopularDestination


@admin.register(PopularDestination)
class PopularDestinationAdmin(admin.ModelAdmin):
    list_display = ['id', 'city_name']
    