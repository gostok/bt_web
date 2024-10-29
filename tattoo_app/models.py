from django.db import models
from django.core.exceptions import ValidationError
from home_app.models import SidebarNews, HeaderImage


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class TattooHeaderImage(HeaderImage):
    pass


class TattooSidebarNews(SidebarNews):
    pass


def validate_image_gallery(image):
    if image.width != 500 or image.height != 600:
        raise ValidationError("Разрешение изображения должно быть 500х600 пикселей.")


class Master(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, related_name="masters", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name


class MasterImage(models.Model):
    master = models.ForeignKey(Master, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="master_images/", validators=[validate_image_gallery]
    )


class Tattoo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    master = models.ForeignKey(
        Master, related_name="tattoos", on_delete=models.CASCADE, null=True
    )
    category = models.ForeignKey(
        Category, related_name="tattoos", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.title


class TattooImage(models.Model):
    tattoo = models.ForeignKey(Tattoo, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="tattoo_images/", validators=[validate_image_gallery]
    )
