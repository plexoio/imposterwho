from django.contrib import admin
from homepage.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "role",
        "type",
        "status",
    )

    list_filter = ("role", "type", "status")
    search_fields = ["username", "email", "role", "type", "status"]

    ordering = ("-id",)


admin.site.register(UserProfile, UserProfileAdmin)
