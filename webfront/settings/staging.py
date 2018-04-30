import os
from webfront.settings.basic import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

# X_FRAME_OPTIONS = 'DENY'
# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# CSRF_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 1
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'HOST': 'psqldb',
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'PORT': 5432,
    }
}

URLS = {
    'auth': 'http://authserver:8000/',
    'base': 'https://localhost:10003/',
    'main': 'https://localhost:10003/main/'
}
