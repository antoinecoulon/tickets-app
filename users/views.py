from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = request.user
    data = {
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "entreprise": {
            'id': user.entreprise.id,
            'nom': user.entreprise.nom
        } if user.entreprise else None,
    }

    return Response(data)
