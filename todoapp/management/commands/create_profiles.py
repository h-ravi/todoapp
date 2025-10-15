from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from todoapp.models import UserProfile

class Command(BaseCommand):
    help = 'Create profiles for existing users'

    def handle(self, *args, **kwargs):
        users_without_profile = []
        for user in User.objects.all():
            if not hasattr(user, 'profile'):
                users_without_profile.append(user)
                # Determine role based on user status
                if user.is_superuser:
                    role = 'superadmin'
                elif user.is_staff:
                    role = 'admin'
                else:
                    role = 'user'
                
                UserProfile.objects.create(user=user, role=role)
                self.stdout.write(self.style.SUCCESS(f'Created profile for {user.username} with role: {role}'))
        
        if not users_without_profile:
            self.stdout.write(self.style.SUCCESS('All users already have profiles!'))
        else:
            self.stdout.write(self.style.SUCCESS(f'\nCreated {len(users_without_profile)} profile(s)'))
