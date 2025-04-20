# Django Imports
from django.urls import path

# Views
from .views import AIChatTemplateView

urlpatterns = [
    path("ai/chat/", AIChatTemplateView.as_view(), name="ai_chat"),
]
