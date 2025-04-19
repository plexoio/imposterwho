from admin_dashboard.common_imports import method_decorator
from django_ratelimit.decorators import ratelimit


class RateLimitStrictMixin:
    """Applies a strict rate limit of 60 GET requests per minute per IP."""

    @method_decorator(
        ratelimit(key="ip", rate="60/m", method="GET", block=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class RateLimitNormalMixin:
    """Applies a normal rate limit of 100 GET requests per minute per IP."""

    @method_decorator(
        ratelimit(key="ip", rate="100/m", method="GET", block=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
