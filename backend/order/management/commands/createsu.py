# images/management/commands/createsu.py

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(email='admin@example.com').exists():
            User.objects.create_superuser(email='admin@example.com',name='admin', password='admin12345678')
            print('Superuser has been created.')
        else:
            print('Superuser already exists.')