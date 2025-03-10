from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Usuario(AbstractUser):
    TIPO_USUARIO = [
        ('cliente', 'Cliente'),
        ('mecanico', 'Mecânico'),
        ('oficina', 'Oficina'),
    ]
    
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=255, blank=True, null=True)

    # Adicionando related_name para evitar conflitos
    groups = models.ManyToManyField(Group, related_name="usuarios", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="usuarios", blank=True)

class Oficina(models.Model):
    dono = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="oficina")
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    cnpj = models.CharField(max_length=18, unique=True)
    
    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco_estimado = models.DecimalField(max_digits=10, decimal_places=2)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, related_name="servicos")

    def __str__(self):
        return f"{self.nome} - {self.oficina.nome}"

# Modelo para mecânicos vinculados às oficinas
class Mecanico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="mecanico")
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, related_name="mecanicos")

    def __str__(self):
        return self.usuario.username

# Modelo para agendamentos de serviços
class Agendamento(models.Model):
    STATUS_OPCOES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="agendamentos")
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, related_name="agendamentos")
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_OPCOES, default='pendente')

    def __str__(self):
        return f"{self.cliente.username} - {self.servico.nome} ({self.status})"

# Modelo para avaliações de oficinas e mecânicos
class Avaliacao(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="avaliacoes")
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE, null=True, blank=True, related_name="avaliacoes")
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE, null=True, blank=True, related_name="avaliacoes")
    nota = models.PositiveIntegerField()
    comentario = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Avaliação {self.nota}/5 por {self.cliente.username}"