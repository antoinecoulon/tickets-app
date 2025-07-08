import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from core.models import Ticket

User = get_user_model()

@pytest.mark.django_db
def test_client_can_create_ticket(client_user):
    client = APIClient()
    client.force_authenticate(user=client_user)

    data = {
        "titre": "Problème connexion",
        "description": "Impossible de me connecter",
        "priorite": "haute",
        "statut": "ouvert"
    }

    response = client.post(reverse("tickets-list"), data)
    assert response.status_code == status.HTTP_201_CREATED
    assert Ticket.objects.filter(titre="Problème connexion").exists()

@pytest.mark.django_db
def test_client_cannot_delete_ticket(client_user, ticket_owned_by_client):
    client = APIClient()
    client.force_authenticate(user=client_user)

    response = client.delete(reverse("tickets-detail", args=[ticket_owned_by_client.id]))
    assert response.status_code == status.HTTP_403_FORBIDDEN

@pytest.mark.django_db
def test_agent_can_edit_ticket(agent_user, ticket_in_same_company):
    client = APIClient()
    client.force_authenticate(user=agent_user)

    response = client.patch(reverse("tickets-detail", args=[ticket_in_same_company.id]), {"statut": "en_cours"})
    assert response.status_code == status.HTTP_200_OK
    assert response.data["statut"] == "en_cours"
