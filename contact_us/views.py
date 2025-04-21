import requests

from admin_dashboard.common_imports import (
    settings,
    JsonResponse,
    TemplateView,
    render,
)


class ContactUsView(TemplateView):
    template_name = "contact.html"  # Define the template for rendering

    def post(self, request, *args, **kwargs):
        """
        Handle the POST request for contact form submission and reCAPTCHA validation.
        """
        recaptcha_response = request.POST.get("g-recaptcha-response")
        data = {"secret": settings.RECAPTCHA_SECRET_KEY, "response": recaptcha_response}
        verify_url = "https://www.google.com/recaptcha/api/siteverify"
        response = requests.post(verify_url, data=data)
        result = response.json()

        # Validate reCAPTCHA response
        if result.get("success"):
            return JsonResponse({"message": "Success!"})
        else:
            return JsonResponse({"error": "Invalid reCAPTCHA. Try again."})

    def get_context_data(self, **kwargs):
        """
        Return context data for the template, if needed.
        """
        context = super().get_context_data(**kwargs)
        # Add any additional context if necessary
        return context
