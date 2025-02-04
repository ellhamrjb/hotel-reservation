from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

class CustomUserTests(TestCase):
    
    def setUp(self):
        self.user_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'username': 'john_doe',
            'password1': 'password123',
            'password2': 'password123'
        }

    def test_create_user(self):
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirect on successful registration
        self.assertTrue(CustomUser.objects.filter(username='john_doe').exists())

    def test_login_user(self):
        user = CustomUser.objects.create_user(**self.user_data)
        response = self.client.post(reverse('login'), {'username': 'john_doe', 'password': 'password123'})
        self.assertEqual(response.status_code, 200)  # Login page should be displayed
