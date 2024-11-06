from typing import Any
from .models import SiteStatistics


class TrackVisitsMiddleware:
    """
    Middleware для отслеживания посещений сайта.

    Этот middleware увеличивает счетчик общего числа посещений сайта
    при каждом запросе. Он создает или получает объект SiteStatistics
    для хранения статистики посещений.

    """

    def __init__(self, get_response):
        """
        Инициализирует middleware и создает объект SiteStatistics,
        если он не существует.

        """

        self.get_response = get_response
        SiteStatistics.objects.get_or_create(id=1)

    def __call__(self, request):
        """
        Обрабатывает входящий запрос, увеличивает счетчик посещений
        и передает управление следующему обработчику.

        """

        stats = SiteStatistics.objects.get(id=1)
        stats.total_visits += 1
        stats.save()

        response = self.get_response(request)
        return response
