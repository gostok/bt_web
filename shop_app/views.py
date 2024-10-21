from django.shortcuts import render
from .models import *


def shop(request):
    sidebar_news = SidebarNews.objects.all()
    shop_header_images = ShopHeaderImage.objects.first()

    context = {
        "sidebar_news": sidebar_news,
        "shop_header_images": shop_header_images,
    }
    return render(request, "shop.html", context)
