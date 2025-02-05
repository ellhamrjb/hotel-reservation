from rest_framework import serializers
from .models import Reservation, MealPlan
from datetime import timezone

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = ['id', 'name', 'description', 'price']
        read_only_fields = ['id']

class ReservationSerializer(serializers.ModelSerializer):
    meal_plan = MealPlanSerializer()
    
    class Meta:
        model = Reservation
        fields = ['id', 'user', 'room', 'check_in', 'check_out', 'guests', 'meal_plan', 'total_price', 'status', 'created_at']
        read_only_fields = ['id', 'total_price', 'status', 'created_at']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
    
    def validate_check_in(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Check-in date cannot be in the past.")
        return value