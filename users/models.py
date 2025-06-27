from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('agent', 'Agent'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='client'
    )

    entreprise = models.ForeignKey(
        'core.Entreprise',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
