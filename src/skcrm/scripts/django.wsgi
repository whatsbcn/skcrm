import os
import sys

paths = ['/var/lib/django/skcrm/src/skcrm/skcrm/', '/var/lib/django/skcrm/src/skcrm/']
for path in paths:
        if path not in sys.path:
                sys.path.append(path)

os.environ['PYTHON_EGG_CACHE'] = '/var/tmp'
os.environ['DJANGO_SETTINGS_MODULE'] = 'apps.settings_prod'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
