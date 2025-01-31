from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
from rest_framework.permissions import AllowAny

class RoomListView(generics.ListAPIView):
    queryset = Room.objects.filter(is_available=True)
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]
