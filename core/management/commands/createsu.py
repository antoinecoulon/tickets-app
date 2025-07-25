from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from decouple import config

class Command(BaseCommand):
    help = 'Create default superuser if not exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = config("DJANGO_SUPERUSER_USERNAME", default="admin_user")
        email = config("DJANGO_SUPERUSER_EMAIL", default="admin@example.com")
        password = config("DJANGO_SUPERUSER_PASSWORD", default="admin_pass")

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
        else:
            self.stdout.write("Superuser already exists")