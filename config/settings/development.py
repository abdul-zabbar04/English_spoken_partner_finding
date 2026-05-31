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