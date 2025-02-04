from rest_framework import generics, permissions
from .models import Payment
from .serializers import PaymentSerializer

class PaymentListView(generics.ListAPIView):
    """ all the payments of a user """
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(reservation__user=self.request.user)
    
class PaymentDetailView(generics.RetrieveAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Payment.objects.filter(reservation__user=self.request.user)

