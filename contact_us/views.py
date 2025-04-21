import requests
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
        verify_url = "https://www.google.com/recaptcha/api/siteverify"
        response = requests.post(verify_url, data=data)
        result = response.json()

        if result.get("success"):

            return JsonResponse({"message": "Success!"})
        else:
            return JsonResponse({"error": "Invalid reCAPTCHA. Try again."})

    return JsonResponse({"error": "Invalid request method"})

def contact_us(request):
    return render(request, "contact_us/contact.html")