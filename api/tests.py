from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from .models import User


class TestUserListTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("user-list")

    def test_list_users(self):
        response = self.client.get(self.url, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        pass
