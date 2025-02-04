from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'phone_number', 'is_guest', 'address', 'date_of_birth', 'profile_picture']
        read_only_fields = ['id']
