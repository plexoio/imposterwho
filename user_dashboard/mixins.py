from admin_dashboard.common_imports import (
    UserPassesTestMixin,
    method_decorator,
    login_required,
)


@method_decorator(login_required, name="dispatch")
class UserRequiredMixin(UserPassesTestMixin):
    """Restricts access to views for users with the 'user' role (role == 0)."""

    def test_func(self):
        user_profile = self.request.user
        return user_profile and user_profile.role == 0
