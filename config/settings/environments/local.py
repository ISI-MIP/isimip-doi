DEBUG = True

SECRET_KEY = 'this is not a secret key'

LOG_LEVEL = 'INFO'
LOG_PATH = 'log'

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
            'filename': f'{LOG_PATH}/error.log',
            'formatter': 'default'
        },
        'django_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/django.log',
            'formatter': 'default'
        },
        'isimip_doi_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/isimip_doi.log',
            'formatter': 'name'
        },
        'django_datacite_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/django_datacite.log',
            'formatter': 'name'
        },
        'general_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': f'{LOG_PATH}/general.log',
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
