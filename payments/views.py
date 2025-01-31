from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer
from .services import request_payment, verify_payment

class PaymentRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data.get("amount")
        if not amount:
            return Response({"error": "Amount is required"}, status=400)

        authority = request_payment(amount, "Hotel Booking Payment", request.user.email, "")
        if authority:
            payment = Payment.objects.create(user=request.user, amount=amount, authority=authority, status="pending")
            return Response({"redirect_url": f"https://www.zarinpal.com/pg/StartPay/{authority}"})
        return Response({"error": "Failed to initiate payment"}, status=400)

class PaymentVerifyView(APIView):
    def get(self, request):
        authority = request.GET.get("Authority")
        status = request.GET.get("Status")
        payment = get_object_or_404(Payment, authority=authority)

        if status == "OK":
            response = verify_payment(authority, payment.amount)
            if response.get("data") and response["data"].get("code") == 100:
                payment.transaction_id = response["data"]["ref_id"]
                payment.status = "completed"
                payment.save()
                return Response({"message": "Payment successful", "transaction_id": payment.transaction_id})
        payment.status = "failed"
        payment.save()
        return Response({"error": "Payment failed"}, status=400)
