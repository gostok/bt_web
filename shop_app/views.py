from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


def shop(request):
    sidebar_news = SidebarNews.objects.all()
    shop_header_images = ShopHeaderImage.objects.first()
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 12)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    context = {
        "sidebar_news": sidebar_news,
        "shop_header_images": shop_header_images,
        "products": products,
    }
    return render(request, "shop.html", context)
