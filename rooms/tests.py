from django.test import TestCase
from .models import Room

class RoomTests(TestCase):
    
    def setUp(self):
        self.room_data = {
            'room_number': '101',
            'room_type': 'single',
            'price': 100.0,
            'available': True
        }

    def test_create_room(self):
        response = self.client.post('/rooms/', self.room_data)
        self.assertEqual(response.status_code, 201)  # Room should be created
        self.assertTrue(Room.objects.filter(room_number='101').exists())

    def test_room_search(self):
        Room.objects.create(**self.room_data)
        response = self.client.get('/rooms/', {'room_type': 'single'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '101')
