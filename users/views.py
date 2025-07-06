from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from core.permissions import IsAdmin
from rest_framework.response import Response
from core.models import Ticket, Entreprise

User = get_user_model()

class AdminStatsView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        tickets_total = Ticket.objects.count()
        agents_total = User.objects.filter(role='agent').count()
        clients_total = User.objects.filter(role='client').count()
        entreprises_total = Entreprise.objects.count()

        tickets_by_statut = {
            "ouvert": Ticket.objects.filter(statut="ouvert").count(),
            "en_cours": Ticket.objects.filter(statut="en_cours").count(),
            "resolu": Ticket.objects.filter(statut="resolu").count(),
            "ferme": Ticket.objects.filter(statut="ferme").count(),
        }

        return Response({
            "tickets_total": tickets_total,
            "agents_total": agents_total,
            "clients_total": clients_total,
            "entreprises_total": entreprises_total,
            "tickets_by_statut": tickets_by_statut
        })

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
