from django.urls import path
from .views import current_user, agents_list

urlpatterns = [
    path('auth/credentials/', current_user),
    path('auth/agents/', agents_list)
]
