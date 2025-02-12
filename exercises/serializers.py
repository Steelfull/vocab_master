from rest_framework import serializers
from .models import ExerciseType, Exercise, ExerciseItem

class ExerciseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseType
        fields = ['id', 'name', 'description']

class ExerciseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseItem
        fields = ['id', 'word', 'question', 'correct_answer', 'user_answer', 'is_correct']

class ExerciseSerializer(serializers.ModelSerializer):
    items = ExerciseItemSerializer(many=True, read_only=True)

    class Meta:
        model = Exercise
        fields = ['id', 'user', 'exercise_type', 'created_at', 'completed', 'items']
        
# exercises/serializers.py
class ExerciseFeedbackSerializer(serializers.Serializer):
    is_correct = serializers.BooleanField()
    correct_answer = serializers.CharField()
    explanation = serializers.CharField()
    progress_change = serializers.FloatField()