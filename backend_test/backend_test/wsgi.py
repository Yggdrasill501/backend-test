"""
WSGI config for backend_test project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""
import os

import django.core.wsgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_test.settings')

application = django.core.wsgi.get_wsgi_application()
