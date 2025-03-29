from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User

class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

       
        if not username or not email or not password:
            return Response({'error': 'Nome de usuário, email e senha são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

       
        if User.objects.filter(email=email).exists():
            return Response({'error': 'Usuário já existe.'}, status=status.HTTP_400_BAD_REQUEST)

        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return Response({'detail': 'Usuário criado com sucesso.'}, status=status.HTTP_201_CREATED)