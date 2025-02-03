from django.contrib import admin
from .models import Room

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'room_type', 'price_per_night', 'capacity', 'is_available')
    search_fields = ('number', 'room_type')
    list_filter = ('room_type', 'is_available')