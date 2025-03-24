from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
