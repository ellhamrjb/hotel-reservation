from rest_framework import generics
from .models import Room, RoomType
from .serializers import RoomSerializer, RoomTypeSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

class RoomTypeListView(generics.ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class RoomListView(generics.ListAPIView):
    """available rooms """
    queryset = Room.objects.filter(available=True)
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]

class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [AllowAny]


class RoomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100