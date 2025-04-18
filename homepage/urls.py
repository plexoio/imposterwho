# Django Imports
from django.urls import path
from django.conf import settings

# Role Redirect
from . import role_redirect

# USER ROLE
path(
    "role_redirect/",
    role_redirect.UserRoleRedirectView.as_view(),
    name="role_redirect",
),
