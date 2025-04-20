# Django Imports
from django.urls import path

# Views
from .views import AIChatTemplateView, LLMInteractionView

urlpatterns = [
    # Chat Template
    path("chat/", AIChatTemplateView.as_view(), name="ai_chat"),
    # LLM Interaction
    path("llm/", LLMInteractionView.as_view(), name="llm_interact"),
]
