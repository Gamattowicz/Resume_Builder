from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class LoginTestCase(TestCase):
    def setUp(self):
        user_1 = User(username="test1", email="test1@gmail.com")
        user_1_password = "test123"
        self.user_1_password = user_1_password
        user_1.is_staff = True
        user_1.is_superuser = True
        user_1.set_password(user_1_password)
        user_1.save()
        self.user_1 = user_1

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)

    def test_user_password(self):
        user_1 = User.objects.get(username="test1")
        self.assertTrue(user_1.check_password(self.user_1_password))

    def test_login_url(self):
        data = {"username": "test1", "password": "test123"}
        response = self.client.post("/users/login/", data, follow=True)
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertRedirects(
            response,
            "/",
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
