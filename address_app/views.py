from django.shortcuts import render
from .models import *


def address(request):
    header_image = HeaderImage.objects.first()
    sidebar_news = SidebarNews.objects.all()
    context = {
        "header_image": header_image,
        "sidebar_news": sidebar_news,
    }
    return render(request, "address.html", context)
