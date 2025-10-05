import os
from pathlib import Path
import dj_database_url
from django.core.management.utils import get_random_secret_key



BASE_DIR = Path(__file__).resolve().parent.parent

#SECRET_KEY = os.environ.get('SECRET_KEY', get_random_secret_key())
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

#ALLOWED_HOSTS = ['*']  # en producción podés poner ['tu-app.onrender.com']
ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    os.environ.get("RENDER_EXTERNAL_HOSTNAME", "localhost")
).split(",")

INSTALLED_APPS = [
    'afiliados',  # tu app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGIN_REDIRECT_URL = '/afiliados/'
LOGOUT_REDIRECT_URL = '/login/'
ROOT_URLCONF = 'celesteyblanca.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'celesteyblanca.wsgi.application'
ASGI_APPLICATION = 'celesteyblanca.asgi.application'

# Base de datos
if os.environ.get('RENDER'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get("DATABASE_URL"),
            conn_max_age=600,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
]

LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
LOGIN_URL = '/afiliados/login/'
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
