from django.test import TestCase, Client
from django.contrib.auth.models import User

class UserAuthenticationTest(TestCase):
    def setUp(self):
        # Создаем тестового пользователя
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.client = Client()

    def test_login(self):
        # Попытка входа с правильными учетными данными
        login_response = self.client.post('/login/', {'username': self.username, 'password': self.password})
        self.assertEqual(login_response.status_code, 200)
        self.assertTrue(login_response.context['user'].is_authenticated)

    def test_login_with_wrong_credentials(self):
        # Попытка входа с неправильными учетными данными
        login_response = self.client.post('/login/', {'username': self.username, 'password': 'wrongpassword'})
        self.assertEqual(login_response.status_code, 200)
        self.assertFalse(login_response.context['user'].is_authenticated)

    def test_logout(self):
        # Вход в систему
        self.client.login(username=self.username, password=self.password)
        # Выход из системы
        logout_response = self.client.get('/logout/')
        self.assertEqual(logout_response.status_code, 200)
        self.assertFalse('_auth_user_id' in self.client.session)
