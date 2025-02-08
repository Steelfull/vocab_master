from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),  # Django Admin
    path('', include('vocab_app.urls')),  # Startseite (vocab_app)
    path('users/', include('users.urls')),  # Benutzerverwaltung
    path('vocabulary/', include('vocabulary.urls')),  # Vokabel-Datenbank
    path('exercises/', include('exercises.urls')),  # Grammatik-Übungen
    path('stats/', include('stats.urls')),  # Statistiken
]