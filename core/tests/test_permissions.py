import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

@pytest.mark.django_db
def test_client_cannot_edit_other_company_ticket(client_user, ticket_of_other_client):
    client = APIClient()
    client.force_authenticate(user=client_user)

    response = client.patch(reverse("tickets-detail", args=[ticket_of_other_client.id]), {"statut": "ferme"})
    assert response.status_code == status.HTTP_403_FORBIDDEN
