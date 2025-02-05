
import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer

ZARINPAL_MERCHANT_ID = "YOUR_MERCHANT_ID"
ZARINPAL_REQUEST_URL = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZARINPAL_VERIFY_URL = "https://api.zarinpal.com/pg/v4/payment/verify.json"
CALLBACK_URL = "http://127.0.0.1:8000/payments/verify/"

class PaymentRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        amount = request.data.get("amount")
        reservation_id = request.data.get("reservation_id")
        reservation = request.user.reservations.filter(id=reservation_id).first()
        
        if not reservation:
            return Response({"error": "Reservation not found"}, status=400)

        payment = Payment.objects.create(
            user=request.user, 
            reservation=reservation, 
            amount=amount, 
            status="pending"
        )

        data = {
            "merchant_id": ZARINPAL_MERCHANT_ID,
            "amount": amount,
            "callback_url": CALLBACK_URL,
            "description": f"Payment for reservation {reservation.id}",
        }
        response = requests.post(ZARINPAL_REQUEST_URL, json=data)
        result = response.json()

        if result["data"]["code"] == 100:
            payment.transaction_id = result["data"]["authority"]
            payment.save()
            return Response({"url": f"https://www.zarinpal.com/pg/StartPay/{result['data']['authority']}"})
        else:
            return Response({"error": "Payment request failed"}, status=400)

class PaymentVerifyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        authority = request.GET.get("Authority")
        payment = Payment.objects.filter(transaction_id=authority, user=request.user).first()
        
        if not payment:
            return Response({"error": "Transaction not found"}, status=400)

        data = {
            "merchant_id": ZARINPAL_MERCHANT_ID,
            "amount": payment.amount,
            "authority": authority,
        }
        response = requests.post(ZARINPAL_VERIFY_URL, json=data)
        result = response.json()

        if result["data"]["code"] == 100:
            payment.status = "success"
            payment.reference_id = result["data"]["ref_id"]
            payment.save()
            return Response({"message": "Payment successful", "ref_id": result["data"]["ref_id"]})
        else:
            payment.status = "failed"
            payment.save()
            return Response({"error": "Payment verification failed"}, status=400)
