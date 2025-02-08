from django.db import models
from users.models import CustomUser

class UserStatistic(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='statistics')
    total_exercises_completed = models.PositiveIntegerField(default=0)
    total_correct_answers = models.PositiveIntegerField(default=0)
    total_incorrect_answers = models.PositiveIntegerField(default=0)

    def update_statistics(self, is_correct):
        """Aktualisiert die Statistiken basierend auf der Benutzerantwort."""
        self.total_exercises_completed += 1
        if is_correct:
            self.total_correct_answers += 1
        else:
            self.total_incorrect_answers += 1
        self.save()

    def __str__(self):
        return f"{self.user.username} - Correct: {self.total_correct_answers}, Incorrect: {self.total_incorrect_answers}"