# users/urls.py
from django.urls import path
from .views import LoginAPIView, RegisterView, get_csrf_token, LogoutAPIView, check_auth


urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("csrf_token/", get_csrf_token, name="csrf_token"),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('check-session/', check_auth, name='check_session'), 
]