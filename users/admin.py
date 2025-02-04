from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'phone_number', 'is_guest', 'is_staff', 'is_active')
    list_filter = ('is_guest', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone_number')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
