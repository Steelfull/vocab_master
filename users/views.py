from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.middleware.csrf import get_token

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
# users/views.py
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
# users/views.py
from rest_framework import permissions


from rest_framework.decorators import api_view

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# users/views.py
@api_view(['GET'])
@permission_classes([AllowAny])
def check_auth(request):
    if request.user.is_authenticated:
        return Response({'status': 'authenticated'})
    return Response({'status': 'unauthenticated'}, status=401)


def get_csrf_token(request):
    print("Aktuelle Cookies:", request.COOKIES)
    token = get_token(request)
    response = JsonResponse({'csrfToken': token})
    response.set_cookie(
        'csrftoken',
        token,
        secure=False,
        samesite='Lax',
        httponly=False,
        path='/'
    )
    print("Gesetztes Cookie:", response.cookies)
    return response

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)  # Optional: Direkt einloggen nach Registrierung
            return Response(serializer.data, status=201)




class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return Response({
                'message': 'Login erfolgreich',
                'redirect': '/dashboard'  # Redirect-Ziel hinzufügen
            }, status=200)
        return Response(
            {'error': 'Ungültige Anmeldedaten'},
            status=401
        )
            
            


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Nur authentifizierte Benutzer können sich ausloggen

    def post(self, request):
        logout(request)  # Django's eingebaute Logout-Funktion
        return Response({"message": "Logout erfolgreich"}, status=status.HTTP_200_OK)