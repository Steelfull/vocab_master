from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# views.py in deinem users-App-Verzeichnis
from django.http import JsonResponse
from django.contrib.auth import logout



class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({'message': 'Login erfolgreich'}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Ungültige Anmeldedaten'},
                status=status.HTTP_401_UNAUTHORIZED
            )