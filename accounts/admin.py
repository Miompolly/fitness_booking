from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Trainer, Fitness, Booking

# Custom User model admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'role', 'date_of_birth', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'role']
    search_fields = ['username', 'email']
    ordering = ['username']
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'date_of_birth', 'role')}),
    )

# Trainer model admin
class TrainerAdmin(admin.ModelAdmin):
    list_display = ['name', 'experience', 'specialty']
    search_fields = ['name', 'specialty']

# Fitness Program model admin
class FitnessAdmin(admin.ModelAdmin):
    list_display = ['name', 'trainer', 'difficulty_level', 'duration_weeks', 'created_at']
    list_filter = ['difficulty_level', 'trainer']
    search_fields = ['name', 'trainer__name']

# Booking model admin
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'fitness_program', 'trainer', 'booking_date', 'time_slot', 'status']
    list_filter = ['status', 'trainer', 'fitness_program']
    search_fields = ['user__username', 'fitness_program__name', 'trainer__name']

# Register the models with the admin site
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Fitness, FitnessAdmin)
admin.site.register(Booking, BookingAdmin)
