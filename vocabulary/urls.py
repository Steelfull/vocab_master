from django.urls import path
from .views import (
    GermanWordListCreateAPIView,
    DeclinationListCreateAPIView,
    ArticleListCreateAPIView,
    PronounListCreateAPIView,
    ConjunctionListCreateAPIView,
    GenerateMetadataAPIView,
    AddWordView
)

urlpatterns = [
    path('words/', GermanWordListCreateAPIView.as_view(), name='word-list-create'),
    path('declinations/', DeclinationListCreateAPIView.as_view(), name='declination-list-create'),
    path('articles/', ArticleListCreateAPIView.as_view(), name='article-list-create'),
    path('pronouns/', PronounListCreateAPIView.as_view(), name='pronoun-list-create'),
    path('conjunctions/', ConjunctionListCreateAPIView.as_view(), name='conjunction-list-create'),
    path('generate-metadata/', GenerateMetadataAPIView.as_view(), name='generate-metadata'),
    path('add-word/', AddWordView.as_view(), name='add-word'),
]