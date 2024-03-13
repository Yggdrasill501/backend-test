# -*- coding: utf-8 -*-
"""Settings for databases."""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'youruser',
        'PASSWORD': 'yourpassword',
        'HOST': 'db',  # Use the service name defined in docker-compose.yml
        'PORT': '5432',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://redis:6379'
    }
}
