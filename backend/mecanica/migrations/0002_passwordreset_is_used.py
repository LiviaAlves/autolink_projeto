# Generated by Django 5.1.7 on 2025-03-25 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mecanica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordreset',
            name='is_used',
            field=models.BooleanField(default=False),
        ),
    ]
