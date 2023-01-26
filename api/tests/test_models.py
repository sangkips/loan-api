from django.test import TestCase
from api.models import CustomUser


class UserTest(TestCase):
    def create_user(self):
        user = CustomUser.objects.create(
            username="newuser",
            email="newuser@email.com",
            first_name="new",
            last_name="user",
        )
        user.set_password("mystrgpasswd")
        user.save()

        self.assertEqual(str(user), "LoanAPI")
