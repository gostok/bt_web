from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


def home(request):
    """
    Обрабатывает запрос к странице 'Главная' и возвращает соответствующий шаблон.
    Настройка пагинации для blog_posts.
    Контекст:
    - carousel_images: модель карусели;
    - blog_posts: модель новостных карточек;
    - sidebar_news: общая модель из home_app.
    """
    carousel_images = CarouselImage.objects.all()
    blog_posts = BlogPost.objects.all().order_by("-published_date")

    paginator = Paginator(blog_posts, 3)
    page_number = request.GET.get("page")
    blog = paginator.get_page(page_number)

    sidebar_news = SidebarNews.objects.all()
    context = {
        "carousel_images": carousel_images,
        "blog_posts": blog,
        "sidebar_news": sidebar_news,
    }
    return render(request, "index.html", context)
