from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Verify admin credentials and show all admin users'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('=' * 70))
        self.stdout.write(self.style.SUCCESS('ADMIN USERS VERIFICATION'))
        self.stdout.write(self.style.SUCCESS('=' * 70))
        
        admins = User.objects.filter(is_staff=True)
        
        if not admins.exists():
            self.stdout.write(self.style.ERROR('❌ No admin users found!'))
            return
        
        self.stdout.write(f'\n✅ Found {admins.count()} admin user(s):\n')
        
        for admin in admins:
            self.stdout.write('-' * 70)
            self.stdout.write(f'👤 Username: {admin.username}')
            self.stdout.write(f'📧 Email: {admin.email}')
            self.stdout.write(f'✓ Is Staff: {admin.is_staff}')
            self.stdout.write(f'✓ Is Superuser: {admin.is_superuser}')
            self.stdout.write(f'✓ Is Active: {admin.is_active}')
            
            if hasattr(admin, 'profile'):
                self.stdout.write(f'🎭 Role: {admin.profile.get_role_display()}')
                self.stdout.write(f'📱 Phone: {admin.profile.phone or "Not set"}')
            else:
                self.stdout.write(self.style.WARNING('⚠️  No profile found'))
            
            self.stdout.write(f'📅 Joined: {admin.date_joined.strftime("%Y-%m-%d %H:%M:%S")}')
            
            if admin.last_login:
                self.stdout.write(f'🕐 Last Login: {admin.last_login.strftime("%Y-%m-%d %H:%M:%S")}')
            else:
                self.stdout.write('🕐 Last Login: Never')
            
            self.stdout.write('')
        
        self.stdout.write('=' * 70)
        self.stdout.write(self.style.SUCCESS('\n📍 LOGIN URLS:'))
        self.stdout.write(self.style.SUCCESS('   User Login: http://127.0.0.1:8000/login/'))
        self.stdout.write(self.style.SUCCESS('   Admin Panel: http://127.0.0.1:8000/admin/'))
        self.stdout.write('=' * 70)
        
        # Show default credentials
        default_admin = User.objects.filter(username='admin').first()
        if default_admin:
            self.stdout.write('\n' + self.style.WARNING('🔑 DEFAULT ADMIN CREDENTIALS:'))
            self.stdout.write(self.style.WARNING(f'   Username: admin'))
            self.stdout.write(self.style.WARNING(f'   Password: admin'))
            self.stdout.write(self.style.WARNING(f'   Email: admin@admin.com'))
            self.stdout.write('')
