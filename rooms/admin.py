from django.contrib import admin
from .models import Room, RoomType

class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'base_price')
    search_fields = ('name',)
    ordering = ('name',)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_night', 'available', 'capacity')
    list_filter = ('available', 'room_type')
    search_fields = ('room_number',)
    ordering = ('room_type', 'room_number')

admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(Room, RoomAdmin)
