from typing import Any
from .models import SiteStatistics


class TrackVisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        SiteStatistics.objects.get_or_create(id=1)

    def __call__(self, request):
        stats = SiteStatistics.objects.get(id=1)
        stats.total_visits += 1
        stats.save()

        response = self.get_response(request)
        return response
