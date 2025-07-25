from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import TicketViewSet, MessageViewSet, AdminMessageListView, AdminEntrepriseListView, AdminUtilisateursListView, EntrepriseDetailView
from django.urls import path, include

# Router principal
router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='tickets')

# Router imbriqué : /tickets/<ticket_pk>/messages/
tickets_router = NestedDefaultRouter(router, r'tickets', lookup='ticket')
tickets_router.register(r'messages', MessageViewSet, basename='ticket-messages')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(tickets_router.urls)),
    path('admin/messages/', AdminMessageListView.as_view(), name='admin-messages'),
    path('admin/entreprises/', AdminEntrepriseListView.as_view(), name='admin-entreprises'),
    path('admin/users/', AdminUtilisateursListView.as_view(), name='admin-users'),
    path('entreprise/', EntrepriseDetailView.as_view(), name='entreprise-detail'),
]
