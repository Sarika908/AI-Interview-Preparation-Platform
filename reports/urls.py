from django.urls import path
from .views import interview_report

urlpatterns = [
    path("", interview_report, name="report"),
]