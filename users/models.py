from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Erweiterte Felder
    language_level = models.CharField(
        max_length=20,
        choices=[('A1', 'Anfänger'), ('B2', 'Fortgeschritten'), ('C2', 'Experte')],
        default='A1'
    )
    premium_member = models.BooleanField(default=False)
    last_activity = models.DateTimeField(auto_now=True)