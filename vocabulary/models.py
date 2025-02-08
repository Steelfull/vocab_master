from django.db import models

from django.db import models
from users.models import CustomUser

class GermanWord(models.Model):
    WORD_CLASS_CHOICES = [
        ('NOUN', 'Substantiv'),
        ('VERB', 'Verb'),
        ('ADJ', 'Adjektiv'),
        ('CONJ', 'Konjunktion'),
        ('PREP', 'Präposition'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    base_form = models.CharField(max_length=100)  # Z.B. "haben"
    word_class = models.CharField(max_length=50, choices=WORD_CLASS_CHOICES)
    gender = models.CharField(max_length=10, null=True, blank=True)  # Für Nomen
    metadata = models.JSONField()  # ChatGPT-Antworten werden hier gespeichert

    def __str__(self):
        return f"{self.base_form} ({self.get_word_class_display()})"

class Declination(models.Model):
    word = models.ForeignKey(GermanWord, on_delete=models.CASCADE)
    case = models.CharField(max_length=20, choices=[
        ('nominativ', 'Nominativ'),
        ('akkusativ', 'Akkusativ'),
        ('dativ', 'Dativ'),
        ('genitiv', 'Genitiv')
    ])
    singular = models.CharField(max_length=100)
    plural = models.CharField(max_length=100)  