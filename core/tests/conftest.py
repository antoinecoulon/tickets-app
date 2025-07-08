# core/tests/conftest.py

import pytest
from users.models import User
from core.models import Ticket, Entreprise

@pytest.fixture
def entreprise():
    return Entreprise.objects.create(nom="TestCorp")

@pytest.fixture
def client_user(entreprise):
    return User.objects.create_user(
        username="client_user",
        email="client@test.com",
        password="testpass123",
        role="client",
        entreprise=entreprise
    )

@pytest.fixture
def agent_user(entreprise):
    return User.objects.create_user(
        username="agent_user",
        email="agent@test.com",
        password="testpass123",
        role="agent",
        entreprise=entreprise
    )

@pytest.fixture
def other_agent():
    # Agent d’une autre entreprise
    other_entreprise = Entreprise.objects.create(nom="OtherCorp", siret="987654321", domaine="Finance")
    return User.objects.create_user(
        username="other_agent",
        email="other@test.com",
        password="testpass123",
        role="agent",
        entreprise=other_entreprise
    )

@pytest.fixture
def admin_user():
    return User.objects.create_user(
        username="admin_user",
        email="admin@test.com",
        password="adminpass",
        role="admin"
    )

@pytest.fixture
def client_ticket(client_user):
    return Ticket.objects.create(
        titre="Bug critique",
        description="Impossible d'accéder au tableau de bord",
        priorite="haute",
        statut="ouvert",
        client=client_user
    )

@pytest.fixture
def ticket_in_same_company(client_user):
    return Ticket.objects.create(
        titre="Test ticket",
        description="Ceci est un ticket test",
        priorite="moyenne",
        statut="ouvert",
        client=client_user
    )

@pytest.fixture
def ticket_owned_by_client(db, client_user):
    return Ticket.objects.create(
        titre="Test Ticket",
        description="Test Description",
        priorite="moyenne",
        statut="ouvert",
        client=client_user,
    )

@pytest.fixture
def ticket_in_other_company(db, other_agent):
    return Ticket.objects.create(
        titre="Ticket étranger",
        description="Doit être inaccessible",
        priorite="basse",
        statut="ouvert",
        client=other_agent,
    )

@pytest.fixture
def ticket_of_other_client(db):
    from core.models import Ticket, Entreprise
    from django.contrib.auth import get_user_model

    User = get_user_model()

    autre_entreprise = Entreprise.objects.create(nom="Autre Entreprise")

    other_client = User.objects.create_user(
        username="client_etranger",
        email="etranger@test.com",
        password="test123",
        role="client",
        entreprise=autre_entreprise,
        first_name="Étranger",
        last_name="Client"
    )

    return Ticket.objects.create(
        titre="Ticket externe",
        description="Un ticket qui ne devrait pas être modifiable",
        priorite="moyenne",
        statut="ouvert",
        client=other_client,
    )
