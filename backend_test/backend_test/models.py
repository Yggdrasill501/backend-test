# -*- coding: utf-8 -*-
"""Models for Rest api."""
import django.db.models


class User(django.db.models.Model):
    """Class users."""

    def __init__(self):
        """Initialize."""
        self.name = django.db.models.CharField(max_length=255)
        self.registered_at = django.db.models.DateTimeField()

    def __str__(self):
        """Return name."""
        return self.name

    def __doc__(self):
        """Return documentation."""
        return self.name.__doc__
