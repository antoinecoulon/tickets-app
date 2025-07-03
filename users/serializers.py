from rest_framework import serializers
from models import User
from core.models import Entreprise

class EntrepriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entreprise
        fields = ['id', 'nom']

class UserSerializer(serializers.ModelSerializer):
    entreprise = EntrepriseSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'entreprise']
