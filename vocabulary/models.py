from django.db import models
from users.models import CustomUser

class GermanWord(models.Model):
    NOUN = "NOUN"
    VERB = "VERB"
    ADJ = "ADJ"
    CONJ = "CONJ"
    PREP = "PREP"
    
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
    gender = models.CharField(max_length=20, null=True, blank=True)  # Für Nomen
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

class Article(models.Model):
    ARTICLE_TYPE_CHOICES = [
        ('definite', 'Bestimmter Artikel'),
        ('indefinite', 'Unbestimmter Artikel'),
    ]
    article_type = models.CharField(max_length=20, choices=ARTICLE_TYPE_CHOICES)
    case = models.CharField(max_length=20, choices=[
        ('nominativ', 'Nominativ'),
        ('akkusativ', 'Akkusativ'),
        ('dativ', 'Dativ'),
        ('genitiv', 'Genitiv')
    ])
    gender = models.CharField(max_length=10)
    singular = models.CharField(max_length=100)
    plural = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_article_type_display()} ({self.case}, {self.gender})"

class Pronoun(models.Model):
    PRONOUN_TYPE_CHOICES = [
        ('personal', 'Personalpronomen'),
        ('possessive', 'Possessivpronomen'),
        ('demonstrative', 'Demonstrativpronomen'),
        ('relative', 'Relativpronomen'),
        ('interrogative', 'Fragepronomen'),
    ]
    pronoun_type = models.CharField(max_length=20, choices=PRONOUN_TYPE_CHOICES)
    case = models.CharField(max_length=20, choices=[
        ('nominativ', 'Nominativ'),
        ('akkusativ', 'Akkusativ'),
        ('dativ', 'Dativ'),
        ('genitiv', 'Genitiv')
    ])
    gender = models.CharField(max_length=10)
    singular = models.CharField(max_length=100)
    plural = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.get_pronoun_type_display()} ({self.case}, {self.gender})"

class Conjunction(models.Model):
    CONJUNCTION_TYPE_CHOICES = [
        ('coordinating', 'Nebenordnende Konjunktion'),
        ('subordinating', 'Unterordnende Konjunktion'),
    ]
    conjunction_type = models.CharField(max_length=20, choices=CONJUNCTION_TYPE_CHOICES)
    case_governed = models.CharField(max_length=20, choices=[
        ('nominativ', 'Nominativ'),
        ('akkusativ', 'Akkusativ'),
        ('dativ', 'Dativ'),
        ('genitiv', 'Genitiv')
    ])
    word = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.word} ({self.get_conjunction_type_display()}, regiert {self.case_governed})"