from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Ticket, Message
from .serializers import TicketSerializer, MessageSerializer

class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
