from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import PasswordReset
import logging
from rest_framework.exceptions import ValidationError
from ..models import Empresa

logger = logging.getLogger(__name__)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email não encontrado.")
        return value
    
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    reset_code = serializers.CharField(max_length=6)
    new_password = serializers.CharField(min_length=6)

    def validate(self, attrs):
        email = attrs.get("email")
        reset_code = attrs.get("reset_code")
        new_password = attrs.get("new_password")

        try:
            user = User.objects.get(email=email)
           
            password_reset = PasswordReset.objects.get(user=user, reset_code=reset_code)

            if not password_reset.is_valid():
                raise serializers.ValidationError("Código expirado ou inválido.")

            if user.check_password(new_password):  
                print("A nova senha não pode ser igual à atual.") 
                raise serializers.ValidationError("A nova senha não pode ser igual à atual.")

            user.set_password(new_password)
            user.save()

        except User.DoesNotExist:
            raise serializers.ValidationError("Usuário não encontrado.")
        except PasswordReset.DoesNotExist:
            raise serializers.ValidationError("Código inválido ou expirado.")

        return attrs
    

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'