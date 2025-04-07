from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from mecanica.models import PasswordReset
from django.utils import timezone
from datetime import timedelta

class ForgotPasswordViewTest(APITestCase):

    def test_forgot_password_user_not_found(self):
        response = self.client.post('/api/forgot-password/', {'email': 'naoexiste@exemplo.com'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)
        self.assertEqual(response.data['email'][0], 'Email não encontrado.')

    def test_forgot_password_valid_user(self):
        user = User.objects.create_user(username='usuario1', email='usuario1@exemplo.com', password='senha123')
        response = self.client.post('/api/forgot-password/', {'email': 'usuario1@exemplo.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Código enviado para seu email!')

class ResetPasswordViewTest(APITestCase):

    def test_reset_password_invalid_code(self):
        user = User.objects.create_user(username='usuario1', email='usuario1@exemplo.com', password='senha123')
        reset_code = '123456'
        response = self.client.post('/api/reset-password/', {'email': 'usuario1@exemplo.com', 'reset_code': reset_code, 'new_password': 'novasenha123'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
        self.assertEqual(response.data['non_field_errors'][0], 'Código inválido ou expirado.')

    def test_reset_password_user_not_found(self):
        response = self.client.post('/api/reset-password/', {'email': 'naoexiste@exemplo.com', 'reset_code': '123456', 'new_password': 'novasenha123'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('non_field_errors', response.data)
        self.assertEqual(response.data['non_field_errors'][0], 'Usuário não encontrado.')

    def test_reset_password_valid(self):
        user = User.objects.create_user(username='usuario1', email='usuario1@exemplo.com', password='senha123')
        password_reset = PasswordReset.objects.create(user=user, reset_code='123456', expires_at=timezone.now() + timedelta(hours=1))
        response = self.client.post('/api/reset-password/', {'email': 'usuario1@exemplo.com', 'reset_code': '123456', 'new_password': 'novasenha123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Senha alterada com sucesso!')

class UserRegistrationTest(APITestCase):

    def test_create_account_valid(self):
        data = {
            'username': 'usuario1',
            'email': 'usuario1@exemplo.com',
            'password': 'senha123'
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('detail', response.data)
        self.assertEqual(response.data['detail'], 'Usuário criado com sucesso.')

    def test_create_account_invalid(self):
        data = {
            'email': 'usuario1@exemplo.com',
            'password': 'senha123',
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)
        self.assertEqual(response.data['error'], 'Nome de usuário, email e senha são obrigatórios.')

class UserLoginTest(APITestCase):

    def test_login_valid(self):
        user = User.objects.create_user(username='usuario1', email='usuario1@exemplo.com', password='senha123')
        data = {
            'username': 'usuario1',
            'password': 'senha123'
        }
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_login_invalid(self):
        data = {
            'username': 'usuario_inexistente',
            'password': 'senha_errada'
        }
        response = self.client.post('/api/token/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['detail'], 'Usuário e/ou senha incorreto(s)')

    def test_login_without_credentials(self):
        response = self.client.post('/api/token/', {})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)
        self.assertIn('password', response.data)
