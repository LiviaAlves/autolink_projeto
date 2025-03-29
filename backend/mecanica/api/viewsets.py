from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .serializers import ForgotPasswordSerializer, ResetPasswordSerializer
from django.contrib.auth import update_session_auth_hash
from ..models import PasswordReset
from ..utils import send_reset_email 


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        if not all(k in data for k in ["username", "email", "password"]):
            return Response({"error": "Todos os campos são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=data["username"]).exists():
            return Response({"error": "Usuário já existe."}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            username=data["username"],
            email=data["email"],
            password=make_password(data["password"]),
        )
        return Response({"message": "Usuário registrado com sucesso!"}, status=status.HTTP_201_CREATED)


class ForgotPasswordView(APIView):
    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                user = User.objects.get(email=email)
                send_reset_email(user)
                return Response({"message": "Código enviado para seu email!"}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ResetPasswordView(APIView):
    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            reset_code = serializer.validated_data["reset_code"]
            new_password = serializer.validated_data["new_password"]

            try:
                user = User.objects.get(email=email)
                password_reset = PasswordReset.objects.get(user=user, reset_code=reset_code)

                if not password_reset.is_valid():
                    return Response({"error": "Código inválido ou expirado."}, status=status.HTTP_400_BAD_REQUEST)

                user.set_password(new_password)
                user.save()

                return Response({"message": "Senha alterada com sucesso!"}, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)
            except PasswordReset.DoesNotExist:
                return Response({"error": "Código de reset inválido."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)