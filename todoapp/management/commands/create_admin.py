from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create admin superuser'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@admin.com',
                password='admin'
            )
            self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
            self.stdout.write(self.style.SUCCESS('Username: admin'))
            self.stdout.write(self.style.SUCCESS('Email: admin@admin.com'))
            self.stdout.write(self.style.SUCCESS('Password: admin'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))
