from django.urls import path
from .views import ZarinpalPaymentRequestView, ZarinpalPaymentVerifyView

urlpatterns = [
    path('zarinpal/request/', ZarinpalPaymentRequestView.as_view(), name='zarinpal-request'),
    path('zarinpal/verify/', ZarinpalPaymentVerifyView.as_view(), name='zarinpal-verify'),
]