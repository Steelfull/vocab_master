from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from vocabulary.models import GermanWord
from .models import Exercise, ExerciseItem, ExerciseType
from .serializers import ExerciseSerializer
import random

from .models import ExerciseItem

class SubmitAnswerAPIView(APIView):
    def post(self, request, item_id, *args, **kwargs):
        user_answer = request.data.get('user_answer')

        try:
            exercise_item = ExerciseItem.objects.get(id=item_id)
            is_correct = exercise_item.check_answer(user_answer)
            return Response({'is_correct': is_correct}, status=status.HTTP_200_OK)
        except ExerciseItem.DoesNotExist:
            return Response(
                {'error': 'Übungsaufgabe nicht gefunden.'},
                status=status.HTTP_404_NOT_FOUND
            )

class GenerateExerciseAPIView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        exercise_type_id = request.data.get('exercise_type_id')

        try:
            exercise_type = ExerciseType.objects.get(id=exercise_type_id)
        except ExerciseType.DoesNotExist:
            return Response(
                {'error': 'Übungstyp nicht gefunden.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Erstelle eine neue Übung
        exercise = Exercise.objects.create(user=user, exercise_type=exercise_type)

        # Wähle zufällige Wörter für die Übung aus
        words = GermanWord.objects.filter(user=user)
        if not words.exists():
            return Response(
                {'error': 'Keine Wörter gefunden.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Generiere Übungsaufgaben
        for word in random.sample(list(words), min(5, len(words))):  # Maximal 5 Aufgaben
            question = f"Dekliniere das Wort '{word.base_form}' im Nominativ Singular."
            correct_answer = word.metadata.get('declinations', {}).get('nominativ', {}).get('singular', 'N/A')

            ExerciseItem.objects.create(
                exercise=exercise,
                word=word,
                question=question,
                correct_answer=correct_answer
            )

        # Serialisiere die Übung für die Antwort
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data, status=status.HTTP_201_CREATED)