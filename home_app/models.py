from django.db import models
from django.core.exceptions import ValidationError


def validate_image_blog_carousel(image):
    """функция для валидации в админ панели изображений карусели на странице - 'Главная'"""

    if image.width < 1700 or image.height < 400:
        raise ValidationError(
            "Разрешение изображения должно быть не меньше 1700x400 пикселей."
        )


class CarouselImage(models.Model):
    """Модель карусели на странице - 'Главная'"""

    image = models.ImageField(
        upload_to="carousel_images/", validators=[validate_image_blog_carousel]
    )
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.alt_text


class BlogPost(models.Model):
    """Модель для новостных карточек на странице - 'Главная'"""

    title = models.CharField(max_length=200)
    content = models.TextField()
    short_description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(
        upload_to="blog_images/",
        null=True,
        blank=True,
    )
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SidebarNews(models.Model):
    """Общая модель для всех страниц с карточками рекламы, или быстрых новостей"""

    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class SiteStatistics(models.Model):
    """Модель для просмотра статистики: сколько было произведено GET-запросов"""

    total_visits = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"Кол-во посещений сайта: {self.total_visits}"
