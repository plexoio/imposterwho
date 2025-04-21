# Django Imports
from django.urls import path

# Views
from . import views

urlpatterns = [
    path("", views.ContactUsView.as_view(), name="contact_us"),
]
