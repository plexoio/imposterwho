# Django Imports
from django.urls import path

# Views
from . import views

urlpatterns = [
    path("", views.contact_us, name="contact_us"),
    path("submit/", views.contact_submit, name="contact_submit"),
]