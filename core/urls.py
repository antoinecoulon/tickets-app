from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from .views import TicketViewSet, MessageViewSet
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
]
