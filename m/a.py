import os
from pathlib import Path
from decouple import Config, RepositoryEnv

config = Config(RepositoryEnv(".env"))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY= '_)5(4e&pr98lw+5+a_959n)f$74xdfkb603u&0ja6b^0*7grem'

#SECRET_KEY = os.environ.get("adhikar_SECRET_KEY")
# Read a simple string value from the .env file
DEBUG = os.environ.get('adhikar_DEBUG')


'''
CORS_ALLOWED_ORIGINS = [
'http://localhost:4200',
'https://www.adhikar.net',
'http://localhost:8100/',
'*',

]'''
CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS =[os.environ.get('adhikar_ALLOWED_HOSTS')]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('adhikar_postgres_name'),
        'USER': os.environ.get('adhikar_postgres_user'),
        'PASSWORD':os.environ.get('adhikar_postgres_password'),
        'HOST':os.environ.get('adhikar_postgres_host'),
        'PORT': os.environ.get('adhikar_postgres_port'),
    }
}'''
CRONJOBS = [
    ('*/1 * * * *', 'm.cron.my_backup')
]
'''DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': ''}'''
'''EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('adhikar_EMAIL_HOST')
EMAIL_PORT = os.environ.get('adhikar_EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('adhikar_EMAIL_USE_TLS')
EMAIL_HOST_USER = os.environ.get('adhikar_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('adhikar_EMAIL_HOST_PASSWORD')'''
INTERNAL_IPS = [
    "127.0.0.1",
]

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
'''STATIC_ROOT = os.path.join(BASE_DIR, '')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]'''

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
