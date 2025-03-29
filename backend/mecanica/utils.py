import random
import string
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime, timedelta
from .models import PasswordReset
from django.contrib.auth.models import User
from django.utils.timezone import now

def generate_reset_code():
    return ''.join(random.choices(string.digits, k=6))

def send_reset_email(user):
    reset_code = str(random.randint(100000, 999999)) 
    expires_at = now() + timedelta(hours=1) 
    password_reset = PasswordReset.objects.create(
        user=user,
        reset_code=reset_code,
        expires_at=expires_at
    )

    send_mail(
        'Seu código de recuperação',
        f'O seu código de recuperação é: {reset_code}. Este código expirará em 1 hora.',
        'from@example.com',
        [user.email],
        fail_silently=False,
    )
