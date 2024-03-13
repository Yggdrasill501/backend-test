# -*- coding: utf-8 -*-
"""Urls."""
from django.urls import path, include
from registration_app.views import UserRegistrationStats


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user-registrations/', UserRegistrationStats.as_view(), name='user-registrations'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

