
from django.urls import path
from . import views

urlpatterns = [
    path("PopularDestinations/", views.PopularDestinationView.as_view()),
]