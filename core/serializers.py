from rest_framework import serializers
from .models import Ticket, Message
from users.models import User

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'client']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'contenu', 'created_at', 'auteur', 'auteur_username', 'ticket']
        read_only_fields = ['id', 'created_at', 'auteur', 'auteur_username']
