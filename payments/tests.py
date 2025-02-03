from django.test import TestCase
from payments.models import Payment
from reservations.models import Reservation
from django.contrib.auth import get_user_model

class PaymentTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test1', password='testpassword123')
        self.reservation = Reservation.objects.create(
            user=self.user, room_id=1, check_in='2025-02-01', check_out='2025-02-05',
            number_of_people=2, meal_option='Breakfast', total_price=400
        )

    def test_create_payment(self):
       
        payment = Payment.objects.create(
            reservation=self.reservation, amount=400, payment_method='Credit Card', status='Completed'
        )
        self.assertEqual(payment.amount, 400)
        self.assertEqual(payment.status, 'Completed')

    def test_payment_success_view(self):
        
        payment = Payment.objects.create(
            reservation=self.reservation, amount=400, payment_method='Credit Card', status='Completed'
        )
        response = self.client.get(f'/payments/success/{payment.reservation.id}/')
        self.assertEqual(response.status_code, 200)
