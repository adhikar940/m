SECRET_KEY = '_)5(4e&pr98lw+5+a_959n)f$74xdfkb603u&0ja6b^0*7grem'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
'''
CORS_ALLOWED_ORIGINS = [
'http://localhost:4200',
'https://www.adhikar.net',
'http://localhost:8100',
'*',

]'''
CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'adhikaran',
        'USER': 'postgres',
        'PASSWORD': 'm&mohan',
        'HOST': 'localhost',
        'PORT': '5432',
    }

}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'adhikar869@gmail.com'
EMAIL_HOST_PASSWORD = 'M&mohan869'


ggg
