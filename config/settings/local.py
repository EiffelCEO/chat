from .common import *
from .key_values import *
DEBUG = False

# CORS
CSRF_COOKIE_SECURE=False
SESSION_COOKIE_SECURE=False
CSRF_COOKIE_HTTPONLY=False
SESSION_COOKIE_HTTPONLY=False
SECURE_CROSS_ORIGIN_OPENER_POLICY = None
SESSION_COOKIE_SAMESITE=False
CSRF_COOKIE_SAMESITE=False
CORS_ALLOW_CREDENTIALS=True
CORS_ORIGIN_ALLOW_ALL=True
CSRF_COOKIE_NAME="csrftoken"
CORS_ALLOWED_ORIGINS=["http://api.ssaptalk.com", "https://api.ssaptalk.com","http://127.0.0.1:3000","http://localhost:8000","http://52.78.102.248:8000","http://localhost:3000","http://0.0.0.0:8000", "http://ssaptalk.com", "https://ssaptalk.com"]
CSRF_TRUSTED_ORIGINS=["http://localhost:8000","http://ssaptalk.com","http://127.0.0.1:3000","http://52.78.102.248:8000","http://0.0.0.0:8000","http://localhost:3000","http://*.0.0.0.0:8000","http://*.0.0.0.0","http://*.52.78.102.248:8000","http://*.52.78.102.248"]
#print("Debug is", DEBUG)
ALLOWED_HOSTS = ["*"]
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# Postgres
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT'),
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_root")
#STATIC_ROOT = '/var/www/html/static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = '/var/www/html/media'

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = 'https://api.ssaptalk.com/media/'

