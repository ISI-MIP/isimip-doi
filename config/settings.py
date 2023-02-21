import os

from django.utils.translation import gettext_lazy as _

import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = (os.getenv('DEBUG', 'False').upper() == 'TRUE')

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost 127.0.0.1 ::1').split()

INTERNAL_IPS = ['127.0.0.1']

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.postgres',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_extensions',
    'django_datacite'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': dj_database_url.parse(os.getenv('DATABASE')),
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
  ('en', _('English')),
]

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

BASE_URL = os.getenv('BASE_URL', '').rstrip('/') + '/'

STATIC_URL = BASE_URL + 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CSRF_COOKIE_PATH = BASE_URL
LANGUAGE_COOKIE_PATH = BASE_URL
SESSION_COOKIE_PATH = BASE_URL

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

DOI_PREFIX = '10.48364'

DATACITE_INCLUDE_CITATION = True
DATACITE_DEFAULT_PUBLIC = True
DATACITE_DEFAULT_PUBLISHER = 'ISIMIP Repository'
DATACITE_DEFAULT_SUBJECT_SCHEME = 'NASA/GCMD Earth Science Keywords'
DATACITE_DEFAULT_SUBJECT_SCHEME_URI = 'http://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/sciencekeywords'

LOG_LEVEL = os.getenv('LOG_LEVEL', 'WARNING')
LOG_DIR = os.getenv('LOG_DIR')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s: %(message)s'
        },
        'name': {
            'format': '[%(asctime)s] %(levelname)s %(name)s: %(message)s'
        },
        'console': {
            'format': '[%(asctime)s] %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'error_log': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'formatter': 'default'
        },
        'django_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'django.log'),
            'formatter': 'default'
        },
        'isimip_doi_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'isimip_doi.log'),
            'formatter': 'name'
        },
        'django_datacite_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'django_datacite.log'),
            'formatter': 'name'
        },
        'general_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'general.log'),
            'formatter': 'name'
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'django_log'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_log'],
            'level': 'ERROR',
            'propagate': True
        },
        'isimip_doi': {
            'handlers': ['console', 'isimip_doi_log'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        'django_datacite': {
            'handlers': ['console', 'django_datacite_log'],
            'level': LOG_LEVEL,
            'propagate': False
        },
        '': {
            'handlers': ['console', 'general_log'],
            'level': LOG_LEVEL,
        }
    }
}
