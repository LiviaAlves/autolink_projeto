from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from mecanica.models import PasswordReset
from django.utils import timezone
from datetime import timedelta

class ForgotPasswordViewTest(APITestCase):

    def test_forgot_password_user_not_found(self):
        """Testa se o erro de email não encontrado retorna status 400 ao invés de 404"""
        response = self.client.post('/api/forgot-password/', {'email': 'naoexiste@exemplo.com'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Espera 400
        self.assertIn('email', response.data)  # Verifica chave 'email'
        self.assertEqual(response.data['email'][0], 'Email não encontrado.')  # Mensagem de erro

    def test_forgot_password_valid_user(self):
        """Testa se um código de reset é enviado corretamente para um usuário válido"""
        user = User.objects.create_user(username='usuario1', email='usuario1@exemplo.com', password='senha123')
        response = self.client.post('/api/forgot-password/', {'email': 'usuario1@exemplo.com'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Código enviado para seu email!')

class ResetPasswordViewTest(APITestCase):

    def test_reset_password_invalid_code(self):
        """Testa se o código de reset inválido retorna o status correto"""
        user = User.objects.create_user(username='usuario1', email='usuario1@exemplo.com', password='senha123')
        reset_code = '123456'  # Código inválido
        response = self.client.post('/api/reset-password/', {'email': 'usuario1@exemplo.com', 'reset_code': reset_code, 'new_password': 'novasenha123'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Espera 400 para código inválido
        self.assertIn('non_field_errors', response.data)  # Chave 'non_field_errors'
        self.assertEqual(response.data['non_field_errors'][0], 'Código inválido ou expirado.')

    def test_reset_password_user_not_found(self):
        """Testa se o usuário não encontrado retorna status 400 ao invés de 404"""
        response = self.client.post('/api/reset-password/', {'email': 'naoexiste@exemplo.com', 'reset_code': '123456', 'new_password': 'novasenha123'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)  # Espera 400 para usuário não encontrado
        self.assertIn('non_field_errors', response.data)
        self.assertEqual(response.data['non_field_errors'][0], 'Usuário não encontrado.')

    def test_reset_password_valid(self):
        """Testa se a senha é resetada corretamente"""
        user = User.objects.create_user(username='usuario1', email='usuario1@exemplo.com', password='senha123')
        password_reset = PasswordReset.objects.create(user=user, reset_code='123456', expires_at=timezone.now() + timedelta(hours=1))
        response = self.client.post('/api/reset-password/', {'email': 'usuario1@exemplo.com', 'reset_code': '123456', 'new_password': 'novasenha123'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Senha alterada com sucesso!')

class UserRegistrationTest(APITestCase):

    def test_create_account_valid(self):
        """Testa a criação de uma conta com dados válidos"""
        data = {
            'username': 'usuario1',
            'email': 'usuario1@exemplo.com',
            'password': 'senha123'
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('detail', response.data)  # Verifica se a chave 'detail' está presente
        self.assertEqual(response.data['detail'], 'Usuário criado com sucesso.')  # Verifica a mensagem de sucesso

    def test_create_account_invalid(self):
        """Testa a criação de uma conta com dados inválidos"""
        data = {
            'email': 'usuario1@exemplo.com',
            'password': 'senha123',  # Faltando o 'username'
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)  # Verifica se a chave 'error' está presente
        self.assertEqual(response.data['error'], 'Nome de usuário, email e senha são obrigatórios.')

class UserLoginTest(APITestCase):

    def test_login_valid(self):
        """Testa o login com dados válidos"""
        user = User.objects.create_user(username='usuario1', email='usuario1@exemplo.com', password='senha123')
        data = {
            'username': 'usuario1',
            'password': 'senha123'
        }
        response = self.client.post('/api/token/', data)  # Usando o endpoint correto para login
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)  # Verifica se o token de acesso foi retornado

    def test_login_invalid(self):
        """Testa o login com dados inválidos"""
        data = {
            'username': 'usuario_inexistente',
            'password': 'senha_errada'
        }
        response = self.client.post('/api/token/', data)  # Usando o endpoint correto para login
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Corrigido para 401
        self.assertEqual(response.data['detail'], 'Usuário e/ou senha incorreto(s)')  # Mensagem de erro

    def test_login_without_credentials(self):
        """Testa o login sem credenciais"""
        response = self.client.post('/api/token/', {})  # Enviando dados vazios
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username', response.data)  # Espera-se o erro de campo obrigatório para 'username'
        self.assertIn('password', response.data)  # Espera-se o erro de campo obrigatório para 'password'

