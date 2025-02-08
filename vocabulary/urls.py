from django.urls import path
from . import views
from django.urls import path
from .views import GenerateMetadataAPIView, WordListCreateAPIView

urlpatterns = [
    path('generate-metadata/', GenerateMetadataAPIView.as_view(), name='generate-metadata'),
    path('words/', WordListCreateAPIView.as_view(), name='word-list'),
]