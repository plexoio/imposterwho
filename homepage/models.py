from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = (
    (0, "User"),
    (1, "Admin"),
    (2, "Manager"),
)

USER_TYPE = (
    (0, "Individual"),
    (1, "Business"),
    (2, "Developer"),
)

STATUS = (
    (0, "Draft"),
    (1, "Paused"),
    (2, "Active"),
)


class UserProfile(AbstractUser):
    """
    Extended user profile model with custom attributes specific
    to the application.

    Inherits from Django's AbstractUser and adds additional fields for:
    - User roles and types
    - Account status

    These fields support enhanced user categorization and personalization
    within the app.
    """

    email = models.EmailField(unique=True)
    role = models.IntegerField(
        choices=ROLES,
        default=0,
        db_index=True,
    )
    type = models.IntegerField(
        choices=USER_TYPE,
        default=0,
        db_index=True,
    )
    status = models.IntegerField(
        choices=STATUS,
        default=2,
        db_index=True,
    )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}"
