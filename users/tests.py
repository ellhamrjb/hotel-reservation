from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class AuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password123")

    def test_register_user(self):
        response = self.client.post("/users/register/", {"username": "newuser", "password": "testpass"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        response = self.client.post("/users/login/", {"username": "testuser", "password": "password123"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_logout_user(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post("/users/logout/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
