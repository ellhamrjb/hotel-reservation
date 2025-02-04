from django.test import TestCase
from .models import Reservation, Room
from django.urls import reverse
from django.utils import timezone

class ReservationTests(TestCase):
    
    def setUp(self):
        room = Room.objects.create(room_number='101', room_type='single', price=100.0, available=True)
        self.reservation_data = {
            'room': room.id,
            'check_in': timezone.now().date() + timezone.timedelta(days=1),
            'check_out': timezone.now().date() + timezone.timedelta(days=2),
            'num_of_people': 2,
            'meal_option': 'breakfast'
        }

    def test_create_reservation(self):
        response = self.client.post(reverse('reservation-list'), self.reservation_data)
        self.assertEqual(response.status_code, 201)  # Reservation should be created
        self.assertTrue(Reservation.objects.filter(room_id=self.reservation_data['room']).exists())
