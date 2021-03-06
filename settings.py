# -*- coding: utf-8 -*-

# Django settings for rarog project.
# Для корректной отдачи картинок
# нужен сервер, который отдает статику
# к примеру nginx,

#location /photologue {
#      root   /home/heit/production/djangoprojects/rarog/media;
#      autoindex on;
#      allow 127.0.0.1;
#      deny all;
#}



DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Kirill Kosinov', 'kirill.kosinov@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.

import os.path

DATABASE_NAME = os.path.join(os.path.dirname(__file__), 'rarog.db')
#DATABASE_NAME = 'rarogdb'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'rarog'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'rarog'         # Not used with sqlite3.
#DATABASE_HOST = '127.0.0.1'             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = '5432'             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru'


ugettext = lambda s: s

LANGUAGES = (
  ('ru', ugettext('Russain')),
  ('en', ugettext('English')),
)


CHARACTER_SET= 'UTF-8'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
#MEDIA_ROOT = os.path.join(os.path.dirname(__file__),'media')
MEDIA_ROOT = '/home/heit/production/djangoprojects/rarog/media'

PHOTOLOGUE_DIR = 'photologue'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://localhost'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'y503nk)qn5oa-oygua9_rx%umh@e#9l4%l)x0y%$7_k8@b=2u^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

)

AUTH_PROFILE_MODULE = 'users.UserProfile'

ABSOLUTE_URL_OVERRIDES = {
    'photologue.photo': lambda o: "%s" % o.get_thumbnail_url(),
}

ROOT_URLCONF = 'rarog.urls'

TEMPLATE_DIRS = '/home/heit/production/djangoprojects/rarog/templates'

STATIC_DOC_ROOT = '/home/heit/production/djangoprojects/rarog/media'

GALERY_PATH = '/home/heit/production/djangoprojects/rarog/media/photologue'

WHOOSH_INDEX = '/home/heit/production/djangoprojects/rarog/idx'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.flatpages',
    'django.contrib.sites',
    'django.contrib.admin',
    'photologue',
    'tagging',
    'rarog.users',
    'rarog.news',
    'rarog.firstpage',
    'rarog.entries',
)
