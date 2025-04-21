from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "homepage/index.html"


class userApps(TemplateView):
    template_name = "homepage/user_apps_page.html"
