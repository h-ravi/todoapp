from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Todo, Budget, IndianHoliday, UserProfile


# Inline Profile in User Admin
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ('role', 'phone', 'address')


# Custom User Creation Form with Role
class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES,
        initial='user',
        help_text='Select user role and permissions'
    )
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(required=False, max_length=150)
    last_name = forms.CharField(required=False, max_length=150)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data.get('first_name', '')
        user.last_name = self.cleaned_data.get('last_name', '')
        
        # Set staff status based on role
        role = self.cleaned_data.get('role', 'user')
        if role in ['admin', 'superadmin']:
            user.is_staff = True
        if role == 'superadmin':
            user.is_superuser = True
        
        if commit:
            user.save()
            # Set the role in profile
            if hasattr(user, 'profile'):
                user.profile.role = role
                user.profile.save()
        return user


# Customize User Admin with Profile
class CustomUserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    add_form = CustomUserCreationForm
    
    list_display = ('username', 'email', 'get_role', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'profile__role')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_joined',)
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role'),
        }),
    )
    
    def get_role(self, obj):
        if hasattr(obj, 'profile'):
            return obj.profile.get_role_display()
        return 'No Profile'
    get_role.short_description = 'Role'
    get_role.admin_order_field = 'profile__role'
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Ensure profile exists
        if not hasattr(obj, 'profile'):
            UserProfile.objects.create(user=obj)


# Unregister the default User admin and register custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

# UserProfile Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('user__username', 'user__email', 'phone')
    list_editable = ('role',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('User Information', {'fields': ('user',)}),
        ('Role & Permissions', {'fields': ('role',)}),
        ('Contact Information', {'fields': ('phone', 'address')}),
    )


# Todo Admin
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'get_user_role', 'status', 'priority', 'due_date', 'created_at')
    list_filter = ('status', 'priority', 'created_at', 'user', 'user__profile__role')
    search_fields = ('title', 'description', 'user__username', 'user__email')
    list_editable = ('status', 'priority')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    autocomplete_fields = ['user']
    
    fieldsets = (
        ('Todo Information', {'fields': ('user', 'title', 'description')}),
        ('Status & Priority', {'fields': ('status', 'priority', 'due_date')}),
    )
    
    def get_user_role(self, obj):
        if hasattr(obj.user, 'profile'):
            return obj.user.profile.get_role_display()
        return 'No Role'
    get_user_role.short_description = 'User Role'
    get_user_role.admin_order_field = 'user__profile__role'

# Budget Admin
@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_user_role', 'type', 'category', 'amount', 'date', 'created_at')
    list_filter = ('type', 'category', 'date', 'user', 'user__profile__role')
    search_fields = ('description', 'user__username', 'user__email')
    list_editable = ('type', 'category', 'amount')
    date_hierarchy = 'date'
    ordering = ('-date',)
    autocomplete_fields = ['user']
    
    fieldsets = (
        ('Budget Information', {'fields': ('user', 'type', 'category', 'amount')}),
        ('Details', {'fields': ('description', 'date')}),
    )
    
    def get_user_role(self, obj):
        if hasattr(obj.user, 'profile'):
            return obj.user.profile.get_role_display()
        return 'No Role'
    get_user_role.short_description = 'User Role'
    get_user_role.admin_order_field = 'user__profile__role'

# IndianHoliday Admin
@admin.register(IndianHoliday)
class IndianHolidayAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'year', 'is_national')
    list_filter = ('year', 'is_national')
    search_fields = ('name', 'description')
    list_editable = ('is_national',)
    date_hierarchy = 'date'
    ordering = ('date',)

# Customize admin site
admin.site.site_header = 'Todo App Admin Panel'
admin.site.site_title = 'Todo App Admin'
admin.site.index_title = 'Welcome to Todo App Administration'
