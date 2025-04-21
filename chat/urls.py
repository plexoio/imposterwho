# Django Imports
from django.urls import path

# Views
from .views import AIChatTemplateView, LLMInteractionView

urlpatterns = [
    # Chat Template
    path("chat/", AIChatTemplateView.as_view(), name="llm_chat_page"),
    # LLM Interaction
    path("post/", LLMInteractionView.as_view(), name="llm_post"),
]
