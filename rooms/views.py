from rest_framework import generics
from .models import Room, RoomType
from .serializers import RoomSerializer, RoomTypeSerializer
from rest_framework.pagination import PageNumberPagination

class RoomTypeListView(generics.ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeSerializer

class RoomListView(generics.ListAPIView):
    """available rooms """
    queryset = Room.objects.filter(available=True)
    serializer_class = RoomSerializer

class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class RoomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100