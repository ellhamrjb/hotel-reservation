from rest_framework import serializers
from .models import HomeContent, HotelInfo

class HomeContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeContent
        fields = '__all__'

class HotelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelInfo
        fields = '__all__'
