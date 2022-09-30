from rest_framework.test import APITestCase, APIClient
from .models import User


class AccountTests(APITestCase):

    client = APIClient()

    name = 'test_user'
    email = 'test_user@gmail.com'
    password = '#test@1234#'

    data = data = {'name': name,
                   'email': email,
                   'password': password,
                   }

    def create_user(self):
        return User.objects.create_user(**self.data)

    def test_users_exist(self):
        self.assertEqual(User.objects.count(), 0)
        self.create_user()

    def test_create_user_without_api(self):

        self.user = self.create_user()
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.email, self.email)

    def test_login(self):

        self.user = self.create_user()
        self.assertTrue(self.client.login(
            email=self.email, password=self.password))

    def test_delete_user(self):

        self.user = self.create_user()
        self.user.delete()
        self.assertEqual(User.objects.count(), 0)

