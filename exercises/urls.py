from django.urls import path
from .views import GenerateExerciseAPIView, GenerateCombinationExerciseAPIView

urlpatterns = [
    path('generate-exercise/', GenerateExerciseAPIView.as_view(), name='generate-exercise'),
    path('generate-combination-exercise/', GenerateCombinationExerciseAPIView.as_view(), name='generate-combination-exercise'),
    path('items/<int:item_id>/submit-answer/', SubmitAnswerAPIView.as_view(), name='submit-answer'),
]