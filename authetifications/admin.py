from django.contrib import admin
from django.db import models
from authetifications.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'name', 'last_login')}),
        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    #list_display = ['email', 'name', 'is_staff', 'last_login']
    #list_filter = ['is_staff', 'is_superuser', 'is_active']
    #search_fields = ['email']
    ordering = ['email']
    # filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User)

