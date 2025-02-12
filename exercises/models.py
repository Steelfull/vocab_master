from django.db import models
from vocabulary.models import GermanWord

class ExerciseType(models.Model):
    """Ein Typ von Übung (z.B. Konjugation, Deklination)."""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Exercise(models.Model):
    """Eine spezifische Übung für einen Benutzer."""
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    exercise_type = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.exercise_type.name} - {self.user.username}"

class ExerciseItem(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name='items')
    word = models.ForeignKey(GermanWord, on_delete=models.CASCADE)
    question = models.TextField()  # Die Frage (z.B. "Dekliniere das Adjektiv 'klein' im Nominativ Singular")
    correct_answer = models.TextField()  # Die korrekte Antwort
    user_answer = models.TextField(blank=True, null=True)  # Die Antwort des Benutzers
    is_correct = models.BooleanField(default=False)  # Wurde die Frage richtig beantwortet?

    def check_answer(self, user_answer):
        """Überprüft die Benutzerantwort und speichert das Ergebnis."""
        self.user_answer = user_answer
        self.is_correct = (user_answer.strip().lower() == self.correct_answer.strip().lower())
        self.save()
        return self.is_correct

    def __str__(self):
        return f"{self.question} - {self.exercise.user.username}"
    
    
# exercises/models.py

class ExerciseType(models.Model):
    CATEGORY_CHOICES = [
        ('DECLENSION', 'Deklination'),
        ('CONJUGATION', 'Konjugation'),
        ('SYNTAX', 'Satzbau')
    ]
    
    STRUCTURE_CHOICES = [
        ('ARTICLE_NOUN', 'Artikel + Substantiv'),
        ('PRONOUN_NOUN', 'Pronomen + Substantiv'),
        ('ADJ_NOUN', 'Adjektiv + Substantiv')
    ]
    
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    structure = models.CharField(max_length=20, choices=STRUCTURE_CHOICES)
    # ... bestehende Felder