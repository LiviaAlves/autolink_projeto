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
