from django.urls import path
from . import views
from django.urls import path
from .views import GenerateMetadataAPIView, WordListCreateAPIView, AddWordView

urlpatterns = [
    path('generate-metadata/', GenerateMetadataAPIView.as_view(), name='generate-metadata'),
    path('words/', AddWordView.as_view(), name='add-word'),
]
