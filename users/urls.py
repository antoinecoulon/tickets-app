from django.urls import path
from .views import current_user

urlpatterns = [
    path('auth/credentials/', current_user)
]
