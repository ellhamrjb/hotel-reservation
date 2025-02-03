from django.test import TestCase
from rooms.models import Room

class RoomTests(TestCase):

    def test_create_room(self):
        
        room = Room.objects.create(
            name='Test Room', price_per_night=100, available=True, description='Test Room Description'
        )
        self.assertEqual(room.name, 'Test Room')
        self.assertEqual(room.price_per_night, 100)
        self.assertTrue(room.available)

    def test_room_list(self):
        
        Room.objects.create(name='Room 1', price_per_night=100, available=True, description='Test Room 1')
        response = self.client.get('/rooms/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Room 1')
