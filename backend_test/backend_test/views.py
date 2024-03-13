# -*- coding: utf-8 -*-
"""Views for Rest Api"""
import json

import django.core.cache
import django.db
import rest_framework.response
import rest_framework.views


# pylint: disable=too-few-public-methods
class UserRegistrationStats(rest_framework.views.APIView):
    """Class gets user registration status."""

    def get(self, request):
        """Get user registration.

        :param request: request.
        :rtype: Response."""
        cache_key = "user_registration_stats"
        cache_time = 86400  # time to live in seconds

        if django.core.cache.cache.get(cache_key):
            return rest_framework.response.Response(json.loads(
                django.core.cache.cache.get(cache_key)
                ))
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    date_trunc('month', registered_at) AS month,
                    COUNT(*) AS registration_count
                FROM 
                    registration_app_user
                WHERE 
                    registered_at >= date_trunc('month', CURRENT_DATE) - INTERVAL '1 year'
                    AND registered_at < date_trunc('month', CURRENT_DATE)
                GROUP BY 
                    month
                ORDER BY 
                    month;
            """)
        rows = cursor.fetchall()

        result = [{"month": row[0].strftime("%Y-%m"),
                   "registration_count": row[1]} for row in rows]
        django.core.cache.cache.set(cache_key, json.dumps(result), cache_time)
        return rest_framework.response.Response(result)
