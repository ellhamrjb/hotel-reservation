from rest_framework import serializers
from .models import Room, RoomType

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id', 'name', 'description', 'base_price']
        read_only_fields = ['id']

class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = ['id', 'room_number', 'room_type', 'price_per_night', 'capacity', 'available', 'description', 'images']
        read_only_fields = ['id']
