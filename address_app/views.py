from django.shortcuts import render
from .models import *


def address(request):
    """
    Обрабатывает запрос к странице 'Адрес' и возвращает соответствующий шаблон.
    Контекст:
    - sidebar_news: общая модель из home_app.
    """

    sidebar_news = SidebarNews.objects.all()
    context = {
        "sidebar_news": sidebar_news,
    }
    return render(request, "address.html", context)
