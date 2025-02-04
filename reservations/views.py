from rest_framework import generics, permissions
from .models import Reservation
from .serializers import ReservationSerializer
from rest_framework import viewsets

class ReservationListCreateView(generics.ListCreateAPIView):
    
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """ users can retrieve, update, or cancel their reservation """
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)
    
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.select_related('user', 'room').all()

