from django.urls import path
from .views import coding_test

urlpatterns = [

    path("", coding_test, name="coding")
]