from django.shortcuts import render
from .models import *


def address(request):

    sidebar_news = SidebarNews.objects.all()
    context = {
        "sidebar_news": sidebar_news,
    }
    return render(request, "address.html", context)
