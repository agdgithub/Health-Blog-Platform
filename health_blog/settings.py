import os
from django.core.management.utils import get_random_secret_key

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Generate a new secret key if it's empty
if not os.environ.get('DJANGO_SECRET_KEY'):
    os.environ['DJANGO_SECRET_KEY'] = get_random_secret_key()

# Use the secret key from environment variables
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False

# Define the installed apps
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]

# Define the template directories
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'blog', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

# Define the URL patterns
ROOT_URLCONF = 'health_blog.urls'

# Define the authentication backend
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Define the bcrypt password hasher
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# Define the login URL
LOGIN_URL = '/login/'

# Define the logout URL
LOGOUT_REDIRECT_URL = '/login/'

# Define the allowed hosts
ALLOWED_HOSTS = ['*']  # Adjust according to your deployment

# Database configuration
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'sHbvXBgqFvQpbOonxrLstzCVtsYGwhMH',
        'HOST': 'roundhouse.proxy.rlwy.net',
        'PORT': '46620',
    }
}

MIDDLEWARE = [
    # Other middleware classes...
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', 
     'django.contrib.auth.middleware.AuthenticationMiddleware',  # Add this line
    # Other middleware classes...
]

