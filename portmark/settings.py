
import os
from pathlib import Path
#import django_heroku

import cloudinary
import cloudinary.uploader
import cloudinary.api

from django.contrib.messages import constants as messages
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#CSRF_TRUSTED_ORIGINS= ["https://testingproj434-production.up.railway.app"]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ux4%%570r*q0c1v22!u^=ht(9*!+y)=r37)h2#k!0b-xeox@_f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'admin_soft.apps.AdminSoftDashboardConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'giftweb',
    'accounts',
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.humanize',
    'cloudinary',
    "corsheaders",
    'storages',
    'django_countries',

    #'activity_log'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    
    "corsheaders.middleware.CorsMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'activity_log.middleware.ActivityLogMiddleware'
]

AUTH_USER_MODEL = 'accounts.User'
LOGIN_URL = "/accounts/login/"
#ACTIVITYLOG_EXCLUDE_URLS = ('/admin/activity_log/activitylog', )

ROOT_URLCONF = 'portmark.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'giftweb.custom_context_processors.notifications',
            ],
        },
    },
]

WSGI_APPLICATION = 'portmark.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASE_URL = "postgresql://postgres.uomfkdmgzkgvtcowpekg:Firstwork51a51$@aws-0-eu-central-1.pooler.supabase.com:5432/postgres"

# Configure the default database using the DATABASE_URL
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URL)
}

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'Firstwork51a51$',
        'HOST': 'db.uvnrhzftedoooliigwqm.supabase.co',
        'PORT': '5432',
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 4,  # Change this to your desired minimum password length
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# settings.py
"""
CELERY_BROKER_URL = 'redis://localhost:6379/0'  # Use your actual Redis server URL
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
"""
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
STATICSTORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#django_heroku.settings(locals())

MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success',
    messages.ERROR: 'alert-danger',
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.AccountNoBackend',
    'accounts.backends.CustomAuthBackend',
)


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Cloudinary configuration

cloudinary.config( 
  cloud_name = "dwpqoubdw", 
  api_key = "746427962229227", 
  api_secret = "Mw778m_arBap_WKexphIdoar0dw" 
)

# CKEditor settings
CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_JQUERY_URL = "https://code.jquery.com/jquery-3.6.0.min.js"  # You can use the jQuery version you prefer
CKEDITOR_IMAGE_BACKEND = "pillow"  # Use Pillow for image processing

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        'codeSnippet_theme': 'monokai',
        'toolbar': 'all',
        'extraPlugins': ','.join([
            'codesnippet',
            'widget',
            'dialog',
            'html5video',
            'youtube',  # Add the 'youtube' plugin here
        ]),
        'filebrowserImageUploadUrl': '/ckeditor/upload/',  # This is the URL for image uploads
        'filebrowserUploadUrl': '/ckeditor/upload/',  # This is the URL for file uploads
    }
}




# Use the SMTP backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.mailersend.net'  # MailerSend SMTP server
EMAIL_PORT = 587                    # Port for TLS
EMAIL_USE_TLS = True                # Use TLS for secure connection
EMAIL_HOST_USER = 'MS_hEOIPz@zorevinacart.store'  # Your MailerSend SMTP username
EMAIL_HOST_PASSWORD = 'iyaHfBTggO1xOkfg'         # Your MailerSend SMTP password
DEFAULT_FROM_EMAIL = 'MS_hEOIPz@zorevinacart.store'  # The default "From" email address
