import os
from pathlib import Path

# Determine the environment file to load
from dotenv import load_dotenv
ENV_FILE = os.getenv("ENV_FILE", ".env")
load_dotenv(dotenv_path=ENV_FILE,override=True)  # Force override system variables

'''
### sqlite database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}'''

'''
### render database 
import dj_database_url  # For parsing DATABASE_URL (optional but recommended)
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('RENDER_DB_URL')  # DATABASE_URL is provided by Render
    )
}
'''

DATABASES = {
    'default': {
        'ENGINE':'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST', 'db'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}

'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("SQL_NAME"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("HOST"),
        "PORT": os.environ.get("PORT"),
    }
}'''

'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "test1",
        'USER': "adhikar",
        'PASSWORD':"adhikar@political#123",
        'HOST':"localhost",
        'PORT': 5432,
    }
}'''
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'localhost',  # or '127.0.0.1'
        'PORT': '5432',
    }
}

'''

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
# ┌───────────── minute (0–59)
# │ ┌───────────── hour (0–23)
# │ │ ┌───────────── day of the month (1–31)
# │ │ │ ┌───────────── month (1–12)
# │ │ │ │ ┌───────────── day of the week (0–6) (Sunday to Saturday;
# │ │ │ │ │                                   7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * * <command to execute>
'''
*/5 * * * *: Every 5 minutes
0 */2 * * *: Every 2 hours
0 0 */3 * *: Every 3 days
0 0 1 */6 *: Every 6 months
'''
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': 'backup/'}
 #('*/1 * * * *', 'm.cron.min_job', '>> /tmp/scheduled_job.log'),      # test every min.
CRONJOBS = [   
    ('0 0 * * *', 'm.cron.daily_job'),      # Daily at midnight
    ('0 0 * * 0', 'm.cron.weekly_job'),     # Weekly at midnight on Sunday
    ('0 0 1 * *', 'm.cron.monthly_job'),    # Monthly at midnight on the 1st
    ('0 0 1 1 *', 'm.cron.yearly_job'),     # Yearly at midnight on January 1st

]

'''EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('adhikar_EMAIL_HOST')
EMAIL_PORT = os.environ.get('adhikar_EMAIL_PORT')
EMAIL_USE_TLS = os.environ.get('adhikar_EMAIL_USE_TLS')
EMAIL_HOST_USER = os.environ.get('adhikar_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('adhikar_EMAIL_HOST_PASSWORD')'''
INTERNAL_IPS = [
    "127.0.0.1",
]

