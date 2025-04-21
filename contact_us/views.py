import requests
<<<<<<< HEAD
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse

def contact_submit(request):
    if request.method == "POST":
        recaptcha_response = request.POST.get("g-recaptcha-response")
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
=======

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
>>>>>>> e98722a1f2c427b9f78f165731958a3491b97b9d
        verify_url = "https://www.google.com/recaptcha/api/siteverify"
        response = requests.post(verify_url, data=data)
        result = response.json()

<<<<<<< HEAD
        if result.get("success"):

=======
        # Validate reCAPTCHA response
        if result.get("success"):
>>>>>>> e98722a1f2c427b9f78f165731958a3491b97b9d
            return JsonResponse({"message": "Success!"})
        else:
            return JsonResponse({"error": "Invalid reCAPTCHA. Try again."})

<<<<<<< HEAD
    return JsonResponse({"error": "Invalid request method"})

def contact_us(request):
    return render(request, "contact_us/contact.html")
=======
    def get_context_data(self, **kwargs):
        """
        Return context data for the template, if needed.
        """
        context = super().get_context_data(**kwargs)
        # Add any additional context if necessary
        return context
>>>>>>> e98722a1f2c427b9f78f165731958a3491b97b9d
