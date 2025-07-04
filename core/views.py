from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from .models import Ticket, Message
from .serializers import TicketSerializer, MessageSerializer
from .permissions import IsAdmin, IsClient, CanPostMessage, CanViewMessage, IsAgentOrAdmin, IsOwnerOrSameCompany

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['statut', 'priorite']
    search_fields = ['titre', 'description']
    ordering_fields = ['created_at', 'priorite']

    def get_permissions(self):
        if self.action  == 'create':
            return [IsAuthenticated(), IsClient()]
        elif self.action in ['update', 'partial_update']:
            return [IsAuthenticated(), IsAgentOrAdmin()]
        elif self.action == 'destroy':
            return [IsAuthenticated(), IsAdmin()]
        elif self.action == 'retrieve':
            return [IsAuthenticated(), IsOwnerOrSameCompany()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Ticket.objects.all()
        elif user.role == 'agent':
            return Ticket.objects.filter(client__entreprise=user.entreprise)
        elif user.role == 'client':
            return Ticket.objects.filter(client=user)
        return Ticket.objects.none()

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), CanPostMessage()]
        elif self.action in ['update', 'destroy']:
            return [IsAuthenticated(), IsAdmin()]
        else:
            return [IsAuthenticated(), CanViewMessage()]

    def get_queryset(self):
        return Message.objects.filter(ticket__id=self.kwargs['ticket_pk']).order_by('created_at')
    
    def perform_create(self, serializer):
        ticket_id = self.kwargs.get('ticket_pk')
        ticket = Ticket.objects.get(id=ticket_id)
        serializer.save(auteur=self.request.user, ticket=ticket, ticket_id=self.kwargs['ticket_pk'])

class AdminMessageListView(ListAPIView):
    permission_classes = [IsAdmin]
    serializer_class = MessageSerializer
    queryset = Message.objects.all().order_by('created_at')
