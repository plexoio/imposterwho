# Django Imports
from django.urls import path

# Views
from . import views

urlpatterns = [
    path("contact/", views.ContactUsView.as_view(), name="contact_us"),
]
