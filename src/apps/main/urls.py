
from django.urls import path
from . import views

urlpatterns = [
    path("FAQ/", views.FAQView.as_view()),
    path("NotificationList/", views.NotificationListView.as_view()),
    path("TechFeedBack/", views.TechSupportFeedbackView.as_view()),
]