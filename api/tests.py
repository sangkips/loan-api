from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestUserListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("user-list")

    def authenticate(self):
        self.client.post(
            reverse("register-list"),
            {
                "username": "admin",
                "email": "admin@email.com",
                "first_name": "sam",
                "last_name": "juma",
                "phone_number": "+254789654410",
                "password": "password123",
                "confirm_password": "password123",
            },
        )

    def test_list_users(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        self.authenticate()
