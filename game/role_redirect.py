# Django Imports
from admin_dashboard.common_imports import (
    redirect,
    View,
    method_decorator,
)
from django_ratelimit.decorators import ratelimit


class UserRoleRedirectView(View):
    """
    View to handle redirection based on the user's role.

    This view extends Django's View class and is responsible for
    redirecting users to different URLs based on their assigned
    roles. The role of a user is determined from the `UserProfile`
    model, where different roles are defined as follows:
    - User (role 0): Redirects to "/user/"
    - Admin (role 1): Redirects to "/manager/"
    - Manager (role 2): Redirects to "/manager/"

    If the user role does not match any defined roles, the user
    will be redirected to the User's page by default.

    Attributes:
        None
    """

    @method_decorator(
        ratelimit(key="ip", rate="100/m", method="GET", block=True),
    )
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests and redirect users based on their role.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            HttpResponseRedirect: Redirects the user to a different URL
            based on their role.
        """
        user = request.user

        if user.role == 0:
            return redirect("/user/")
        elif user.role == 1:
            return redirect("/manager/")
        elif user.role == 2:
            return redirect("/manager/")
        else:
            return redirect("/user/")
