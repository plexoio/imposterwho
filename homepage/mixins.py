from admin_dashboard.common_imports import method_decorator, login_required
from django_ratelimit.decorators import ratelimit
from django.contrib.auth.mixins import UserPassesTestMixin


class RateLimitStrictMixin:
    """
    """
    @method_decorator(
        ratelimit(key="ip", rate="60/m", method="GET", block=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class RateLimitNormalMixin:
    """
    """
    @method_decorator(
        ratelimit(key="ip", rate="100/m", method="GET", block=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


@method_decorator(login_required, name="dispatch")
class UserRequiredMixin(UserPassesTestMixin):
    """
    """
    def test_func(self):
        user_profile = self.request.user
        return user_profile and user_profile.role == 0
