# Generated by Django 5.1.7 on 2025-03-10 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('cnpj', models.CharField(max_length=18, unique=True)),
                ('dono', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='oficina', to='api_web.usuario')),
            ],
        ),
    ]
