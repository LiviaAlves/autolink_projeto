# Generated by Django 5.1.7 on 2025-04-08 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mecanica', '0003_remove_passwordreset_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('cpf_responsavel', models.CharField(max_length=14)),
                ('rg_responsavel', models.CharField(max_length=20)),
                ('conta_bancaria', models.CharField(max_length=50)),
                ('horario_funcionamento', models.CharField(max_length=100)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_empresas/')),
            ],
        ),
    ]
