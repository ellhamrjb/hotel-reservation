from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class UserTests(TestCase):

    def test_user_registration(self):
        
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(reverse('users:register'), data)
        self.assertEqual(response.status_code, 302)  
        
        user = get_user_model().objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')

    def test_user_profile(self):
        
        user = get_user_model().objects.create_user(
            username='test1', email='test1@example.com', password='testpassword123'
        )
        self.client.login(username='test1', password='testpassword123')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test1')
