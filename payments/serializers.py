from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'reservation', 'payment_id', 'status', 'amount', 'transaction_date']
        read_only_fields = ['id', 'transaction_date']
