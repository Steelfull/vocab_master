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
        exercise_type = self.get_exercise_type(request.data)
        generator = self.get_generator(exercise_type)
        exercise = generator.generate()
        return Response(exercise.serialize(), status=201)

    def get_generator(self, exercise_type):
        generators = {
            'ARTICLE_NOUN': ArticleNounGenerator,
            'PRONOUN_NOUN': PronounNounGenerator,
            'ADJ_NOUN': AdjectiveNounGenerator
        }
        return generators[exercise_type.structure](self.request.user)
    
    
class BaseExerciseGenerator:
    def __init__(self, user):
        self.user = user
        self.words = GermanWord.objects.filter(user=user)
    
    def generate_question(self, word):
        raise NotImplementedError
        
    def generate(self):
        exercise = Exercise.objects.create(...)
        for word in selected_words:
            question_data = self.generate_question(word)
            ExerciseItem.objects.create(...)
        return exercise
    
class ArticleNounGenerator(BaseExerciseGenerator):
    CASES = ['nominativ', 'akkusativ', 'dativ', 'genitiv']
    NUMBERS = ['singular', 'plural']
    
    def generate_question(self, word):
        case = random.choice(self.CASES)
        number = random.choice(self.NUMBERS)
        
        return {
            'type': 'ARTICLE_NOUN',
            'question': f"Ergänze Artikel und Substantiv im {case} {number}:",
            'hint': {
                'gender': word.gender,
                'case': case,
                'number': number
            },
            'correct_answer': {
                'article': word.metadata['declinations'][case][number]['article'],
                'noun': word.metadata['declinations'][case][number]['form']
            }
        }
        
# exercises/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def user_progress(request):
    completed = Exercise.objects.filter(user=request.user, completed=True).count()
    total = Exercise.objects.filter(user=request.user).count()
    return Response({
        'progress': (completed / total) * 100 if total > 0 else 0,
        'streak': request.user.streak,
        'recent_exercises': ExerciseSerializer(
            Exercise.objects.filter(user=request.user).order_by('-created_at')[:3],
            many=True
        ).data
    })