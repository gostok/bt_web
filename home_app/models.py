from django.db import models
from django.core.exceptions import ValidationError


class CarouselImage(models.Model):
    image = models.ImageField(upload_to="carousel_images/")
    alt_text = models.CharField(max_length=100)

    def __str__(self):
        return self.alt_text


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    short_description = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="blog_images/", null=True, blank=True)
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class SidebarNews(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


def validate_image(image):
    if image.width < 2560 or image.height < 1440:
        raise ValidationError(
            "Разрешение изображения должно быть не меньше 2560х1440 пикселей."
        )


class HeaderImage(models.Model):
    image = models.ImageField(upload_to="header_images/", validators=[validate_image])

    def __str__(self) -> str:
        return "Header Image"


class SiteStatistics(models.Model):
    total_visits = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"Кол-во посещений сайта: {self.total_visits}"
