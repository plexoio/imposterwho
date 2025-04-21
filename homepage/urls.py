# Django Imports
from django.urls import path

# Role Redirect
from . import role_redirect, views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path(
        "redirect/",
        role_redirect.UserRoleRedirectView.as_view(),
        name="role_redirect",
    ),
    path(
        "apps/",
        views.userApps.as_view(),
        name="user_apps",
    ),
]
