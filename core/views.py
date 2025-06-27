from django.shortcuts import render
from rest_framework import viewsets
from .models import Ticket, Message
from .serializers import TicketSerializer, MessageSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
