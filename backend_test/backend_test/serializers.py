# -*- coding: utf-8 -*-
"""Serializers for Rest api."""
import serializers.rest_framework
import backend_test.backend_test.serializers.models


# pylint: disable=too-few-public-methods
class UserSerializer(serializers.rest_framework.serializers.ModelSerializer):
    """User serializer from rest framework."""

    class Meta:
        """Meta class."""

        def __init__(self):
            """Initialize."""
            self.model = backend_test.backend_test.serializers.models.User
            self.fields = ['id', 'name', 'registered_at']
