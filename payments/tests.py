from django.test import TestCase
from .models import Payment

class PaymentTests(TestCase):
    
    def setUp(self):
        self.payment_data = {
            'amount': 150.0,
            'payment_gateway': 'Zarinpal',
            'transaction_id': 'TXN12345'
        }

    def test_create_payment(self):
        response = self.client.post('/payments/', self.payment_data)
        self.assertEqual(response.status_code, 201)  # Payment should be created
        self.assertTrue(Payment.objects.filter(transaction_id='TXN12345').exists())
