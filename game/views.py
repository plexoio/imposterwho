from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView


# Create your views here.
class GamePage(TemplateView):
    template_name = "game/game.html"
