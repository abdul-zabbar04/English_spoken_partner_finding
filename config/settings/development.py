import os
import environ
from .base import *

# Initialize the Env class object
env= environ.Env()

# Read the local root folder .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))



DEBUG = True

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT')
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env('EMAIL_ID')
EMAIL_HOST_PASSWORD = env('APP_PASSWORD')

DEFAULT_FROM_EMAIL = "noreply@englishBuddy.com"

FRONTEND_URL = env("FRONTEND_URL")
