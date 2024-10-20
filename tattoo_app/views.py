from django.shortcuts import render
from .models import *
from home_app.models import SidebarNews


def tattoo(request):
    sidebar_news = SidebarNews.objects.all()
    tattoos = Tattoo.objects.all()
    masters = Master.objects.all()
    context = {
        'sidebar_news': sidebar_news,
        'tattoos': tattoos,
        'masters': masters,
    }
    return render(request, 'tattoo.html', context)