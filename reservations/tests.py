from django.test import TestCase
from django.urls import reverse
from .models import Reservation
from rooms.models import Room
from django.contrib.auth import get_user_model

class ReservationTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword123')
        self.room = Room.objects.create(name='Test Room', price_per_night=100)

    def test_create_reservation(self):
        
        self.client.login(username='test1', password='testpassword123')
        response = self.client.post(reverse('reservations:reserve', args=[self.room.id]), {
            'check_in': '2025-02-01',
            'check_out': '2025-02-05',
            'number_of_people': 2,
            'meal_option': 'Breakfast'
        })
        self.assertEqual(response.status_code, 302)  #  redirects after successful reservation

    def test_reservation_detail(self):
        
        reservation = Reservation.objects.create(
            user=self.user, room=self.room, check_in='2025-02-01', check_out='2025-02-05',
            number_of_people=2, meal_option='Breakfast', total_price=400
        )
        self.client.login(username='test1', password='testpassword123')
        response = self.client.get(reverse('reservations:reservation_detail', args=[reservation.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Reservation Details')
