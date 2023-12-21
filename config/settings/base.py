from pathlib import Path

from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).parent.parent.parent

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '::1']

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
        'DIRS': [BASE_DIR / 'templates'],
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
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'isimip_data'
    },
    'metadata': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'isimip_metadata'
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

LANGUAGE_CODE = 'en-us'

LANGUAGES = [
  ('en', _('English')),
]

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static_root'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend'
]

DOI_PREFIX = '10.48364'

DATACITE_INCLUDE_CITATION = True

DATACITE_DEFAULT_PUBLIC = True

DATACITE_DEFAULT_PUBLISHER = 'ISIMIP Repository'

DATACITE_IDENTIFIER_TYPES = (
    ('DOI', _('DOI')),
    ('URL', _('URL')),
)

DATACITE_RESOURCE_TYPES_GENERAL = (
    ('Book', _('Book')),
    ('ConferencePaper', _('ConferencePaper')),
    ('ConferenceProceeding', _('ConferenceProceeding')),
    ('DataPaper', _('DataPaper')),
    ('Dataset', _('Dataset')),
    ('Dissertation', _('Dissertation')),
    ('Journal', _('Journal')),
    ('JournalArticle', _('JournalArticle')),
    ('PeerReview', _('PeerReview')),
    ('Preprint', _('Preprint')),
    ('Report', _('Report')),
    ('Software', _('Software')),
    ('Text', _('Text')),
    ('Other', _('Other')),
)

DATACITE_DEFAULT_SUBJECT_SCHEME = 'NASA/GCMD Earth Science Keywords'
DATACITE_DEFAULT_SUBJECT_SCHEME_URI = 'http://gcmdservices.gsfc.nasa.gov/kms/concepts/concept_scheme/sciencekeywords'

DATACITE_DEFAULT_CONTRIBUTOR_TYPE = 'ContactPerson'
DATACITE_CONTRIBUTOR_TYPES = (
    ('ContactPerson', _('ContactPerson')),
    ('DataCurator', _('DataCurator')),
    ('HostingInstitution', _('HostingInstitution')),
    ('ProjectLeader', _('ProjectLeader')),
    ('ProjectManager', _('ProjectManager')),
    ('ProjectMember', _('ProjectMember')),
    ('RelatedPerson', _('RelatedPerson')),
    ('Researcher', _('Researcher')),
    ('RightsHolder', _('RightsHolder')),
    ('Other', _('Other')),
)

DATACITE_RELATION_TYPES = (
    ('IsCitedBy', _('IsCitedBy')),
    ('Cites', _('Cites')),
    ('IsSupplementTo', _('IsSupplementTo')),
    ('IsSupplementedBy', _('IsSupplementedBy')),
    ('IsContinuedBy', _('IsContinuedBy')),
    ('Continues', _('Continues')),
    ('IsDescribedBy', _('IsDescribedBy')),
    ('Describes', _('Describes')),
    ('HasMetadata', _('HasMetadata')),
    ('IsMetadataFor', _('IsMetadataFor')),
    ('HasVersion', _('HasVersion')),
    ('IsVersionOf', _('IsVersionOf')),
    ('IsNewVersionOf', _('IsNewVersionOf')),
    ('IsPreviousVersionOf', _('IsPreviousVersionOf')),
    ('IsPartOf', _('IsPartOf')),
    ('HasPart', _('HasPart')),
    ('IsPublishedIn', _('IsPublishedIn')),
    ('IsReferencedBy', _('IsReferencedBy')),
    ('References', _('References')),
    ('IsDocumentedBy', _('IsDocumentedBy')),
    ('Documents', _('Documents')),
    ('IsCompiledBy', _('IsCompiledBy')),
    ('Compiles', _('Compiles')),
    ('IsVariantFormOf', _('IsVariantFormOf')),
    ('IsOriginalFormOf', _('IsOriginalFormOf')),
    ('IsIdenticalTo', _('IsIdenticalTo')),
    ('IsReviewedBy', _('IsReviewedBy')),
    ('Reviews', _('Reviews')),
    ('IsDerivedFrom', _('IsDerivedFrom')),
    ('IsSourceOf', _('IsSourceOf')),
    ('IsRequiredBy', _('IsRequiredBy')),
    ('Requires', _('Requires')),
    ('IsObsoletedBy', _('IsObsoletedBy')),
    ('Obsoletes', _('Obsoletes')),
)
