from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()

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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def agents_list(request):
    user = request.user
    if user.role not in ['admin', 'agent']:
        return Response(status=403)
    
    agents = User.objects.filter(role='agent')
    if user.role == 'agent':
        agents = agents.filter(entreprise=user.entreprise)

    data = [{'id': agent.id, 'username': agent.username} for agent in agents]
    return Response(data)
