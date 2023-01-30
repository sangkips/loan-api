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

        response = self.client.post(
            reverse("token_obtain_pair"),
            {
                "email": "admin@email.com",
                "password": "password123",
            },
        )

        print(response.data)

    def test_list_users(self):
        response = self.client.get(self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        self.authenticate()
