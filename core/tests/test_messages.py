import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from core.models import Message

@pytest.mark.django_db
def test_user_can_create_message(client_user, ticket_owned_by_client):
    client = APIClient()
    client.force_authenticate(user=client_user)

    response = client.post(reverse("ticket-messages-list", kwargs={"ticket_pk": ticket_owned_by_client.id}), {
        "contenu": "Merci pour votre aide"
    })

    assert response.status_code == status.HTTP_201_CREATED
    assert Message.objects.filter(contenu="Merci pour votre aide").exists()

@pytest.mark.django_db
def test_user_can_list_messages(agent_user, ticket_in_same_company):
    client = APIClient()
    client.force_authenticate(user=agent_user)

    response = client.get(reverse("ticket-messages-list", kwargs={"ticket_pk": ticket_in_same_company.id}))
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data["results"], list)
