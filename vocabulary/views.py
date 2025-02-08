from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from openai import OpenAI
from rest_framework.permissions import IsAuthenticated

client = OpenAI()
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI

client = OpenAI()
import json


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openai import OpenAI

client = OpenAI()
import json



from rest_framework import generics
from .models import GermanWord
from .serializers import GermanWordSerializer





class GenerateMetadataAPIView(APIView):
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
            - Wortart
            - Genus (falls Nomen)
            - Konjugationen (Präsens, Präteritum, Perfekt für Verben)
            - Deklinationen (alle vier Kasus für Adjektive/Nomen mit Singular UND Plural)
            - Typische Satzbeispiele
            """

            response = client.chat.completions.create(model="gpt-3.5-turbo",  # Teste mit gpt-3.5-turbo
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7)

            # ChatGPT-Antwort parsen
            metadata = response.choices[0].message.content
            try:
                parsed_metadata = json.loads(metadata)
            except json.JSONDecodeError:
                return Response(
                    {"error": "Ungültiges JSON von ChatGPT"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            return Response({'metadata': parsed_metadata}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {'error': f'Ein Fehler ist aufgetreten: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
            
class WordListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = GermanWordSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Zeigt nur die Wörter des aktuellen Users
        return GermanWord.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Setze den aktuellen Benutzer automatisch
        serializer.save(user=self.request.user)