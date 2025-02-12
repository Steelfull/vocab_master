"""
Django settings for vocab_app project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from dotenv import load_dotenv
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0p95hqv@3$+3aq428!d1##4g=@btdcpu2m1p)r+j7cl-ex7i_m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vocab_app',  # Haupt-App
    'users',  # Benutzerverwaltung
    'vocabulary',  # Vokabel-Datenbank
    'stats',  # Statistiken
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken', 
]



# Lade Umgebungsvariablen aus .env
load_dotenv()

# OpenAI API-Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Muss VOR CSRF sein!
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # Jetzt korrekt nach Session
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    
]


# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
]
}

# settings.py
OPENAI_API_KEY = "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"


ROOT_URLCONF = 'vocab_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'vocab_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vocab_master',
        'USER': 'db_user',  # Der Benutzer, der nicht existiert
        'PASSWORD': 'Basinga!12',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'users.CustomUser'

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',  # React-Frontend
]

SESSION_COOKIE_SECURE = False  # Für HTTP in Entwicklung
SESSION_COOKIE_SAMESITE = 'Lax'  # Erlaubt Cookies für Cross-Origin-Requests
CSRF_COOKIE_SECURE = False
CSRF_COOKIE_SAMESITE = 'Lax'

# Sicherstellen, dass diese Einstellungen existieren
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]
CORS_ALLOW_CREDENTIALS = True  # Wichtig für Cookies
# settings.py
# settings.py (ergänzen)
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',     # Wichtig für CSRF
    'x-requested-with',
    'cookie',  # Explizit erlauben
    'credentials'
]

CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken', 'set-cookie']

SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # bleibt auch nach Schließen des Browsers bestehen
CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS.copy()

# settings.py
SESSION_COOKIE_AGE = 1209600  # 2 Wochen (Standard)
SESSION_SAVE_EVERY_REQUEST = True  # Session bei jedem Request verlängern
SESSION_COOKIE_DOMAIN = 'localhost'  # Explizite Domain für Entwicklung

