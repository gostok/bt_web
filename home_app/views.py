from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def home(request):
    header_image = HeaderImage.objects.first()
    carousel_images = CarouselImage.objects.all()
    blog_posts = BlogPost.objects.all().order_by("-published_date")

    paginator = Paginator(blog_posts, 2)
    page_number = request.GET.get("page")
    blog = paginator.get_page(page_number)

    sidebar_news = SidebarNews.objects.all()
    context = {
        "carousel_images": carousel_images,
        "blog_posts": blog,
        "sidebar_news": sidebar_news,
        "header_image": header_image,
    }
    return render(request, "index.html", context)
