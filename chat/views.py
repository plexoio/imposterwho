from admin_dashboard.common_imports import (
    TemplateView,
    method_decorator,
    ratelimit,
    JsonResponse,
)


class AIChatTemplateView(
    TemplateView,
):
    """ """

    template_name = "ai_chat.html"

    @method_decorator(
        ratelimit(key="ip", rate="10/m", method="GET", block=True),
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Populates additional context for rendering the template.
        """
        context = super().get_context_data(**kwargs)

        return context

    @method_decorator(ratelimit(key="ip", rate="10/m", method="POST", block=True))
    def post(self, request, *args, **kwargs):
        return JsonResponse(
            {
                "status": "error",
                "message": f"{instance_error}!",
            }
        )
