# -*- coding: utf-8 -*-
"""Serializers for Rest api."""
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'registered_at']

