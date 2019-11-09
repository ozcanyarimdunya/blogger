import os
from collections import OrderedDict

from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'si*52#bq8#88qafliumhv#@yge6edq&vn2moy2l4e=t)7b61kc'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party application
    'blogger.apps.common.apps.ConstanceConfig',
    'constance.backends.database',
    'ckeditor',
    'ckeditor_uploader',

    # custom application
    'blogger.apps.common.apps.CommonConfig',
    'blogger.apps.article.apps.ArticleConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blogger.middlewares.StatsMiddleWare',
]

ROOT_URLCONF = 'blogger.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'constance.context_processors.config',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blogger.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets', 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets', 'local')
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SITE_HEADER = "Blogger"

# constance settings
CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}],
    'editor_field': ['ckeditor_uploader.fields.RichTextUploadingFormField', {'required': False}],
}

CONSTANCE_CONFIG = OrderedDict([
    ('SITE_TITLE', ('Hi!', 'Website title')),
    ('SITE_NAME', ('ÖZCAN YARIMDÜNYA', 'Website name')),
    ('SITE_AUTHOR', ('ÖZCAN YARIMDÜNYA', 'Site author')),
    ('SITE_DESCRIPTION', ('Personal Blog', 'Site description')),
    ('SITE_FOOTER_TEXT', ('Copyright © semiworld.org 2019', 'Website footer text')),
    ('SITE_LINKEDIN_URL', ('', 'LinkedIn url')),
    ('SITE_TWITTER_URL', ('', 'Twitter url')),
    ('SITE_GITHUB_URL', ('', 'Github url')),
    ('SITE_STACKOVERFLOW_URL', ('', 'Stackoverflow url')),
    ('HOME_PAGE_TITLE', ('Personal Blog', 'Home page title')),
    ('HOME_PAGE_DESCRIPTION', ('Software Engineer @ Huawei Tech.', 'Home page title description')),
    ('ABOUT_PAGE_TITLE', ('About Me', 'About page title')),
    ('ABOUT_PAGE_SUBTITLE', ('This is what i do.', 'About page subtitle')),
    ('ABOUT_PAGE_SUMMARY', ('A summary about me', 'About page summary', 'editor_field')),
    ('CONTACT_PAGE_TITLE', ('Contact Me', 'Contact page title')),
    ('CONTACT_PAGE_SUBTITLE', ('Have questions? I have answers.', 'Contact page subtitle')),
    ('CONTACT_PAGE_SUMMARY', ('Want to get in touch? Fill out the form below to send me a message and '
                              'I will get back to you as soon as possible!', 'Contact page summary', 'editor_field')),
])

CONSTANCE_CONFIG_FIELDSETS = OrderedDict([
    ('Site Settings', (
        'SITE_TITLE',
        'SITE_NAME',
        'SITE_FOOTER_TEXT',
        'SITE_AUTHOR',
        'SITE_DESCRIPTION',
    )),
    ('Social Links', (
        'SITE_LINKEDIN_URL',
        'SITE_TWITTER_URL',
        'SITE_GITHUB_URL',
        'SITE_STACKOVERFLOW_URL',
    )),
    ('Home Page', (
        'HOME_PAGE_TITLE',
        'HOME_PAGE_DESCRIPTION',
    )),
    ('About Page', (
        'ABOUT_PAGE_TITLE',
        'ABOUT_PAGE_SUBTITLE',
        'ABOUT_PAGE_SUMMARY',
    )),
    ('Contact Page', (
        'CONTACT_PAGE_TITLE',
        'CONTACT_PAGE_SUBTITLE',
        'CONTACT_PAGE_SUMMARY',
    )),
])

CKEDITOR_UPLOAD_PATH = "editor/"

MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

LOGIN_URL = '/admin/login/'
