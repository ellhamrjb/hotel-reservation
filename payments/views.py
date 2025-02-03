import requests
from django.shortcuts import get_object_or_404
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from .models import Payment
from .serializers import PaymentSerializer, ZarinpalPaymentRequestSerializer
from reservations.models import Reservation

ZARINPAL_MERCHANT_ID = "zarinpal_id"  #will be added later
ZARINPAL_REQUEST_URL = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZARINPAL_VERIFY_URL = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZARINPAL_START_URL = "https://www.zarinpal.com/pg/StartPay/"

class ZarinpalPaymentRequestView(generics.GenericAPIView):
    serializer_class = ZarinpalPaymentRequestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        reservation = get_object_or_404(Reservation, id=serializer.validated_data['reservation_id'])
        amount = serializer.validated_data['amount']
        callback_url = serializer.validated_data['callback_url']

        data = {
            "merchant_id": ZARINPAL_MERCHANT_ID,
            "amount": int(amount),  #integer toman
            "callback_url": callback_url,
            "description": f"Payment for Reservation {reservation.id}",
        }

        response = requests.post(ZARINPAL_REQUEST_URL, json=data)
        response_data = response.json()

        if response_data.get("data") and response_data["data"].get("authority"):
            authority = response_data["data"]["authority"]
            payment = Payment.objects.create(
                reservation=reservation,
                amount=amount,
                method="zarinpal",
                status="pending",
                transaction_id=authority,
                callback_url=callback_url
            )
            return Response({"payment_url": f"{ZARINPAL_START_URL}{authority}"}, status=status.HTTP_200_OK)
        else:
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class ZarinpalPaymentVerifyView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        authority = request.GET.get("Authority")
        status_code = request.GET.get("Status")

        payment = get_object_or_404(Payment, transaction_id=authority)

        if status_code == "OK":
            data = {
                "merchant_id": ZARINPAL_MERCHANT_ID,
                "authority": authority,
                "amount": int(payment.amount),
            }

            response = requests.post(ZARINPAL_VERIFY_URL, json=data)
            response_data = response.json()

            if response_data.get("data") and response_data["data"].get("code") == 100:
                payment.status = "completed"
                payment.save()
                return Response({"message": "Payment successful", "ref_id": response_data["data"]["ref_id"]}, status=status.HTTP_200_OK)
            else:
                payment.status = "failed"
                payment.save()
                return Response({"message": "Payment verification failed"}, status=status.HTTP_400_BAD_REQUEST)

        payment.status = "failed"
        payment.save()
        return Response({"message": "Payment failed or canceled"}, status=status.HTTP_400_BAD_REQUEST)