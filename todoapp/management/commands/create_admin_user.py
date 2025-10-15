from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from todoapp.models import UserProfile

class Command(BaseCommand):
    help = 'Create admin users with different roles (superadmin, admin, manager, user)'

    def add_arguments(self, parser):
        parser.add_argument('--username', type=str, help='Username for the admin')
        parser.add_argument('--email', type=str, help='Email for the admin')
        parser.add_argument('--password', type=str, help='Password for the admin')
        parser.add_argument('--role', type=str, default='admin', 
                          choices=['user', 'manager', 'admin', 'superadmin'],
                          help='Role: user, manager, admin, or superadmin')

    def handle(self, *args, **kwargs):
        username = kwargs.get('username')
        email = kwargs.get('email')
        password = kwargs.get('password')
        role = kwargs.get('role')
        
        # Interactive mode if arguments not provided
        if not username:
            username = input('Enter username: ')
        if not email:
            email = input('Enter email: ')
        if not password:
            password = input('Enter password: ')
        if not role:
            self.stdout.write('\nAvailable roles:')
            self.stdout.write('1. user - Regular user (no admin access)')
            self.stdout.write('2. manager - Can manage users and view reports')
            self.stdout.write('3. admin - Full admin access (can manage all data)')
            self.stdout.write('4. superadmin - Super Admin (full system control)')
            role_input = input('\nSelect role (1-4) or type role name [default: admin]: ').strip()
            
            role_map = {
                '1': 'user',
                '2': 'manager',
                '3': 'admin',
                '4': 'superadmin'
            }
            role = role_map.get(role_input, role_input) if role_input else 'admin'
        
        # Validate role
        valid_roles = ['user', 'manager', 'admin', 'superadmin']
        if role not in valid_roles:
            self.stdout.write(self.style.ERROR(f'Invalid role: {role}'))
            self.stdout.write(self.style.ERROR(f'Valid roles are: {", ".join(valid_roles)}'))
            return
        
        # Check if user exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(f'User "{username}" already exists!'))
            update = input('Do you want to update the role? (yes/no): ').lower()
            if update == 'yes':
                user = User.objects.get(username=username)
                
                # Update user permissions based on role
                if role in ['admin', 'superadmin']:
                    user.is_staff = True
                else:
                    user.is_staff = False
                
                if role == 'superadmin':
                    user.is_superuser = True
                else:
                    user.is_superuser = False
                
                user.save()
                
                # Update profile role
                if hasattr(user, 'profile'):
                    user.profile.role = role
                    user.profile.save()
                else:
                    UserProfile.objects.create(user=user, role=role)
                
                self.stdout.write(self.style.SUCCESS(f'User "{username}" updated successfully!'))
                self.stdout.write(self.style.SUCCESS(f'Role: {role}'))
            return
        
        # Create new user
        if role == 'superadmin':
            user = User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
        elif role in ['admin', 'manager']:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            if role == 'admin':
                user.is_staff = True
                user.save()
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
        
        # Set profile role
        if hasattr(user, 'profile'):
            user.profile.role = role
            user.profile.save()
        else:
            UserProfile.objects.create(user=user, role=role)
        
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('User created successfully!'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS(f'Username: {username}'))
        self.stdout.write(self.style.SUCCESS(f'Email: {email}'))
        self.stdout.write(self.style.SUCCESS(f'Password: {password}'))
        self.stdout.write(self.style.SUCCESS(f'Role: {role.upper()}'))
        self.stdout.write(self.style.SUCCESS(f'Staff Status: {user.is_staff}'))
        self.stdout.write(self.style.SUCCESS(f'Superuser Status: {user.is_superuser}'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        
        # Show role permissions
        self.stdout.write('\n' + self.style.WARNING('Role Permissions:'))
        if role == 'superadmin':
            self.stdout.write('✓ Full system control')
            self.stdout.write('✓ Can create/edit/delete any user')
            self.stdout.write('✓ Access to admin panel')
            self.stdout.write('✓ All admin features')
        elif role == 'admin':
            self.stdout.write('✓ Can manage all users and data')
            self.stdout.write('✓ Access to admin panel')
            self.stdout.write('✓ Can create/edit/delete todos and budgets')
        elif role == 'manager':
            self.stdout.write('✓ Can view user reports')
            self.stdout.write('✓ Can manage assigned users')
            self.stdout.write('✓ Limited admin access')
        else:
            self.stdout.write('✓ Regular user access')
            self.stdout.write('✓ Can manage own todos and budgets')
        
        self.stdout.write('\n' + self.style.SUCCESS('Login at: http://127.0.0.1:8000/login/'))
        if user.is_staff:
            self.stdout.write(self.style.SUCCESS('Admin panel: http://127.0.0.1:8000/admin/'))
