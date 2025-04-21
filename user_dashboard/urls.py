from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_dashboard, name='user_dashboard'),
    path('remove_from_favorites/<int:favorite_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]
