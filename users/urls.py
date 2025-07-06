from django.urls import path
from .views import current_user, agents_list, AdminStatsView

urlpatterns = [
    path('auth/credentials/', current_user),
    path('auth/agents/', agents_list),
    path('admin/stats/', AdminStatsView.as_view(), name='admin-stats')
]
