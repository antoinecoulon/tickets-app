from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Ticket, Message, Entreprise
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = "Seed database with sample data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        self.stdout.write(self.style.SUCCESS("Seeding data..."))

        # Créer entreprises
        e1, _ = Entreprise.objects.get_or_create(nom="OpenDev")
        e2, _ = Entreprise.objects.get_or_create(nom="CodeLab")

        # Créer admin
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin1234",
                role="admin"
            )

        # Créer agents
        agents = []
        for i in range(2):
            user, _ = User.objects.get_or_create(
                username=f"agent{i+1}",
                defaults={
                    "email": f"agent{i+1}@opendev.com",
                    "first_name": f"Agent{i+1}",
                    "last_name": "Smith",
                    "role": "agent",
                    "entreprise": e1
                }
            )
            user.set_password("agent1234")
            user.save()
            agents.append(user)

        # Créer clients
        clients = []
        for i in range(3):
            user, _ = User.objects.get_or_create(
                username=f"client{i+1}",
                defaults={
                    "email": f"client{i+1}@opendev.com",
                    "first_name": f"Client{i+1}",
                    "last_name": "Doe",
                    "role": "client",
                    "entreprise": e1
                }
            )
            user.set_password("client1234")
            user.save()
            clients.append(user)

        # Créer tickets
        titres = [
            "Problème de connexion",
            "Erreur sur la page d'accueil",
            "Demande de nouveau mot de passe",
            "Problème de performance",
            "Bug affichage mobile",
            "Impossible de valider le formulaire",
        ]
        priorites = ["basse", "moyenne", "haute"]
        statuts = ["ouvert", "en_cours", "resolu"]

        for i in range(20):
            client = random.choice(clients)
            agent = random.choice(agents)
            ticket = Ticket.objects.create(
                titre=random.choice(titres),
                description="Description détaillée du problème rencontré par l'utilisateur.",
                priorite=random.choice(priorites),
                statut=random.choice(statuts),
                client=client,
                agent=agent,
            )

            # Créer messages
            for j in range(random.randint(1, 3)):
                Message.objects.create(
                    ticket=ticket,
                    auteur=random.choice([client, agent]),
                    contenu="Message automatique de test",
                    created_at=timezone.now()
                )

        self.stdout.write(self.style.SUCCESS("✅ Données insérées avec succès."))
