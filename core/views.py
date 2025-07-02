from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Ticket, Message
from .serializers import TicketSerializer, MessageSerializer
from .permissions import IsTicketOwnerOrAdmin, IsInSameCompanyAsTicket

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Ticket.objects.all()
        elif user.role == 'agent':
            return Ticket.objects.filter(client__entreprise=user.entreprise)
        elif user.role == 'client':
            return Ticket.objects.filter(client=user)
        return Ticket.objects.none()
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['statut', 'priorite']
    search_fields = ['titre', 'description']
    ordering_fields = ['created_at', 'priorite']
    
    def save(self, *args, **kwargs):
        if self.statut:
            self.statut = self.statut.lower()
        if self.priorite:
            self.priorite = self.priorite.lower()
        super().save(*args, **kwargs)

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'client':
            raise PermissionDenied('Seuls les clients peuvent créer des tickets.')
        serializer.save(client=user)

    def perform_update(self, serializer):
        user = self.request.user
        ticket = self.get_object()

        if user.role == 'admin':
            serializer.save()
        elif user.role == 'agent':
            if ticket.client.entreprise != user.entreprise:
                raise PermissionDenied('Vous ne pouver modifier que les tickets de votre entreprise.')
            serializer.save()
        else:
            raise PermissionDenied('Seuls les agents ou admin peuvent modifier un ticket.')
        
    def perform_destroy(self, instance):
        user = self.request.user
        if user.role != 'admin':
            raise PermissionDenied('Seuls les administrateurs peuvent supprimer un ticket.')
        instance.delete()

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Message.objects.all()
        elif user.role == 'client':
            return Message.objects.filter(ticket__client=user)
        elif user.role == 'agent':
            return Message.objects.filter(ticket__client__entreprise=user.entreprise)
        return Message.objects.none()
    
    def perform_create(self, serializer):
        user = self.request.user
        ticket = serializer.validated_data['ticket']

        if user.role == 'client' and ticket.client != user:
            raise PermissionDenied('Vous ne pouvez écrire que sur vos propres tickets.')
        if user.role == 'agent' and ticket.client.entreprise != user.entreprise:
            raise PermissionDenied('Vous ne pouvez écrire que sur les tickets de votre entreprise.')
        serializer.save(auteur=user)
        
    def perform_update(self, serializer):
        user = self.request.user
        if user.role != 'admin':
            raise PermissionDenied('Seul un administrateur peut modifier un message.')
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        if user.role != 'admin':
            raise PermissionDenied('Seul un administrateur peut supprimer un message.')
        instance.delete()

# TODO: tester permissions
