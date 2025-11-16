from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'is_traveler', 'is_admin', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_traveler', 'is_admin', 'is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'phone')
    ordering = ('-date_joined',)

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'is_traveler', 'is_admin')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('phone', 'is_traveler', 'is_admin')}),
    )
