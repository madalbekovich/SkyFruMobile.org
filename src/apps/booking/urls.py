from django.urls import path
from .views import GetOptimalFaresView

urlpatterns = [
    path('GetOptimalFares/', GetOptimalFaresView.as_view()),
]