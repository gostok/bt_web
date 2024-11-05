from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def shop(request):
    sidebar_news = SidebarNews.objects.all()
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 9)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    for product in products:
        product.seller_contacts = product.seller.contacts.all()

    context = {
        "sidebar_news": sidebar_news,
        "products": products,
    }
    return render(request, "shop.html", context)
