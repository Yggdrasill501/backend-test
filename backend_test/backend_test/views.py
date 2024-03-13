# -*- coding: utf-8 -*-
"""Views for Rest Api"""
from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
import json


class UserRegistrationStats(APIView):
    """Class gets user registration status"""

    def get(self, request):
        """Get user registration.

        :param request: request.
        :rtype: Response."""
        cache_key = "user_registration_stats"
        cache_time = 86400  # time to live in seconds

        if cache.get(cache_key):
            # return cached data
            return Response(json.loads(cache.get(cache_key)))
        else:
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

            result = [{"month": row[0].strftime("%Y-%m"), "registration_count": row[1]} for row in rows]
            cache.set(cache_key, json.dumps(result), cache_time)
            return Response(result)
