from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



import json


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json



from rest_framework import generics
from .models import GermanWord
from .serializers import GermanWordSerializer


# vocabulary/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from openai import OpenAI
from rest_framework import permissions

client = OpenAI(api_key="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")


class AddWordView(APIView):
    permission_classes = [permissions.AllowAny] 
    
    def post(self, request):
        serializer = GermanWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Setze den aktuellen Benutzer
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




class GenerateMetadataAPIView(APIView):
    permission_classes = [permissions.AllowAny] 
 
    def post(self, request, *args, **kwargs):
        word = request.data.get('word')

        if not word:
            return Response(
                {'error': 'Das Wort darf nicht leer sein.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # ChatGPT-Anfrage
            prompt = f"""
            Generiere deutsche Grammatikdaten für das Wort '{word}' im JSON-Format.
            Beinhaltet:
            - Wortart (als 'word_class' und folgende Choices: Substantiv = "NOUN", VERB = "VERB", ADJEKTIV = "ADJ", Konjunktion = "CONJ", Präposition = "PREP")
            - Nur bei Nomen: Genus (gender: Femininum, Maskulinum, Neutrum)
            - Konjugationen (Präsens, Präteritum, Perfekt, Futur I/II, Plusquamperfekt für Verben)
            - Deklinationen (alle vier Kasus für Adjektive/Nomen mit Singular UND Plural)
            - Typische Satzbeispiele
            """

            response = client.chat.completions.create(model="gpt-3.5-turbo",  # Teste mit gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7)

            # ChatGPT-Antwort parsen
            try:
                metadata = response.choices[0].message.content.strip()
                parsed_metadata = json.loads(metadata)
            except json.JSONDecodeError:
                return Response({"error": "Ungültiges JSON von ChatGPT"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            

            return Response({'metadata': parsed_metadata}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': f'Ein Fehler ist aufgetreten: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
from rest_framework import generics
from .models import GermanWord, Declination, Article, Pronoun, Conjunction
from .serializers import GermanWordSerializer, DeclinationSerializer, ArticleSerializer, PronounSerializer, ConjunctionSerializer
from rest_framework.permissions import IsAuthenticated

class GermanWordListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = GermanWordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return GermanWord.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DeclinationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DeclinationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Declination.objects.filter(word__user=self.request.user)
    
    def perform_create(self, serializer):
        word_id = self.request.data.get('word')
        word = GermanWord.objects.get(id=word_id, user=self.request.user)
        serializer.save(word=word)

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    queryset = Article.objects.all()

class PronounListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PronounSerializer
    permission_classes = [IsAuthenticated]
    queryset = Pronoun.objects.all()

class ConjunctionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ConjunctionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Conjunction.objects.all()