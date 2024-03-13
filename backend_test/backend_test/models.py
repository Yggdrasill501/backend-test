# -*- coding: utf-8 -*-
"""Models for Rest api."""
from django.db import models


class User(models.Model):
    """Class users."""

    name = models.CharField(max_length=255)
    registered_at = models.DateTimeField()

    def __str__(self):
        """Return name."""
        return self.name

