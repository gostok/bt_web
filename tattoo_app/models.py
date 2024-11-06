from django.db import models
from django.core.exceptions import ValidationError
from home_app.models import SidebarNews


class Category(models.Model):
    """Модель для дропменю Категории на вкладке Татуировки"""

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class TattooSidebarNews(SidebarNews):
    """Связь с общей моделью SidebarNews из home_app"""

    pass


class Master(models.Model):
    """Модель карточек Мастеров, соединенная с моделью Категории"""

    name = models.CharField(max_length=200)
    description = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, related_name="masters", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name


class MasterImage(models.Model):
    """Модель изображений для карточек Мастеров"""

    master = models.ForeignKey(Master, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="master_images/")


class Tattoo(models.Model):
    """Модель карточек Тату работ, соединенная с моделями Мастера и Категории"""

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
    """Модель изображений для карточек Тату работ"""

    tattoo = models.ForeignKey(Tattoo, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="tattoo_images/")
