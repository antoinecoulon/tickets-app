from django.db import models
from django.conf import settings

class Entreprise(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom
    
class Ticket(models.Model):
    STATUT_CHOICES = [
        ('ouvert', 'Ouvert'),
        ('en_cours', 'En cours'),
        ('resolu', 'Résolu'),
        ('ferme', 'Fermé'),
    ]

    PRIORITE_CHOICES = [
        ('basse', 'Basse'),
        ('moyenne', 'Moyenne'),
        ('haute', 'Haute'),
    ]

    titre = models.CharField(max_length=255)
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='ouvert')
    priorite = models.CharField(max_length=10, choices=PRIORITE_CHOICES, default='moyenne')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tickets_clients')
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name='tickets_agents')

    def __str__(self):
        return self.titre
    
class Message(models.Model):
    contenu = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='messages')

    def __str__(self):
        return f"Message de {self.auteur.username} sur {self.ticket.titre}"
