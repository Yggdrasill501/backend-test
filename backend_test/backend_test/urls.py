# -*- coding: utf-8 -*-
"""Urls."""
import django.urls
import registration_app.views

urlpatterns = [
    # pylint: disable=undefined-variable
    django.urls.path('admin/', admin.site.urls),
    django.urls.path('api/user-registrations/', registration_app.views.UserRegistrationStats.as_view(), name='user-registrations'),
    django.urls.path('api-auth/', registration_app.views.include('rest_framework.urls', namespace='rest_framework')),
]
