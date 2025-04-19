from .common_imports import (
    UserPassesTestMixin,
    method_decorator,
    login_required,
    PermissionDenied,
)


@method_decorator(login_required, name="dispatch")
class AdminRequiredMixin(UserPassesTestMixin):
    """Restricts access to views for users with the 'admin' or 'manager' role
    (role == 1 and role == 2)."""

    def test_func(self):
        user_profile = self.request.user
        return user_profile and user_profile.role == 1 or user_profile.role == 2


class ManagerDenyPermissionMixin:
    """Denies access to users with the 'manager' role (role == 2).
    Since the manager will not have access to certain Admin Features.

    - Use this mixin to deny permission to the manager.
    """

    def dispatch(self, request, *args, **kwargs):
        """Checks for manager role before processing the request."""
        self.permission_denied(request)
        response = super().dispatch(request, *args, **kwargs)
        return response

    def permission_denied(self, request):
        """Raises a PermissionDenied error if the user is a manager."""

        user_role = request.user.role
        if user_role == 2:
            raise PermissionDenied("You do not have permission.")
