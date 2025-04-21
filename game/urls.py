# Django Imports
from django.urls import path

# Views
from . import views

urlpatterns = [
    path("", views.GamePage.as_view(), name="game"),
]
