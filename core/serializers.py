from rest_framework import serializers
from .models import Ticket, Message, Entreprise
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TicketSerializer(serializers.ModelSerializer):
    client = UserSummarySerializer(read_only=True)
    agent = UserSummarySerializer(read_only=True)
    agent_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(role='agent'),
        source='agent',
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'client']

class AuteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class MessageSerializer(serializers.ModelSerializer):
    auteur = AuteurSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'contenu', 'created_at', 'auteur']
        read_only_fields = ['id', 'created_at', 'auteur']

class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ['id', 'nom']

class AdminUtilisateursListSerializer(serializers.ModelSerializer):
    entreprise = EntrepriseSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'entreprise']