from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import make_aware

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=6)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    def is_valid(self):
        now = make_aware(datetime.now()) 
        return not self.is_used and self.expires_at > now


class Empresa(models.Model):
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    cpf_responsavel = models.CharField(max_length=14)
    rg_responsavel = models.CharField(max_length=20)
    conta_bancaria = models.CharField(max_length=50)
    horario_funcionamento = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos_empresas/', blank=True, null=True)

    def __str__(self):
        return self.nome_fantasia