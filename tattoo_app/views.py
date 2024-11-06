from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def tattoo(request):
    """
    Обрабатывает запрос к странице 'Татуировки' и возвращает соответствующий шаблон.
    Настройка пагинации для tattoos и masters.
    Настройка Категорий для вкладки tattoos.

    Контекст:
    - tattoos: модель карточек тату работ, основанная на выбранной категории и номере страницы в пагинации;
    - masters: модель карточек мастеров;
    - categories: список всех доступных категорий тату работ;
    - tab: текущая вкладка, по умолчанию 'tattoo';
    - sidebar_news: общая модель из home_app.
    """

    sidebar_news = SidebarNews.objects.all()

    categories = Category.objects.all()

    categories_id = request.GET.get("category")
    if categories_id == "all" or categories_id is None:
        tattoo_list = Tattoo.objects.all()
    else:
        tattoo_list = Tattoo.objects.filter(category_id=categories_id)

    tattoo_paginator = Paginator(tattoo_list, 3)
    tattoo_page_number = request.GET.get("page")
    tattoos = tattoo_paginator.get_page(tattoo_page_number)

    master_list = Master.objects.all()
    master_paginator = Paginator(master_list, 3)
    master_page_number = request.GET.get("master_page")
    masters = master_paginator.get_page(master_page_number)

    tab = request.GET.get("tab", "tattoo")

    context = {
        "sidebar_news": sidebar_news,
        "tattoos": tattoos,
        "masters": masters,
        "categories": categories,
        "tab": tab,
    }
    return render(request, "tattoo.html", context)
