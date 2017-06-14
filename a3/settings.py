from django.conf import settings as django_settings
from a3 import models

SITE_NAME = 'Sample Website'
SITE_URL = 'http://a3.com/'
SITE_IMAGE = 'a3.png'
SITE_STATIC_URL = '//localhost:{}/'.format(django_settings.DEBUG_PORT) if django_settings.DEBUG else '//i.a3.com/'
GAME_NAME = 'Sample Game'
DISQUS_SHORTNAME = 'a3'
ACCOUNT_MODEL = models.Account
COLOR = '#4a86e8'
