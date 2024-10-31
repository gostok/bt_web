from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def tattoo(request):
    header_image = HeaderImage.objects.first()
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
        "header_image": header_image,
        "sidebar_news": sidebar_news,
        "tattoos": tattoos,
        "masters": masters,
        "categories": categories,
        "tab": tab,
    }
    return render(request, "tattoo.html", context)
