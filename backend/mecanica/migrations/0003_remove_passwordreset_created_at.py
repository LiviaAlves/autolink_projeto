# Generated by Django 5.1.7 on 2025-03-25 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mecanica', '0002_passwordreset_is_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordreset',
            name='created_at',
        ),
    ]
