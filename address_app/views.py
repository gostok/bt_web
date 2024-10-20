from django.shortcuts import render
from .models import *
from home_app.models import SidebarNews
def address(request):
    sidebar_news = SidebarNews.objects.all()
    context = {
        'sidebar_news': sidebar_news,
    }
    return render(request, 'address.html', context)
