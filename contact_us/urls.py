# Django Imports
from django.urls import path

# Views
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.contact_us, name="contact_us"),
    path("submit/", views.contact_submit, name="contact_submit"),
]
=======
    path("contact/", views.ContactUsView.as_view(), name="contact_us"),
]
>>>>>>> e98722a1f2c427b9f78f165731958a3491b97b9d
