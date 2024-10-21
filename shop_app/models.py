from django.db import models
from django.core.exceptions import ValidationError
from home_app.models import SidebarNews


class ShopSidebarNews(SidebarNews):
    pass


def validate_image(image):
    if image.width < 2560 or image.height < 1440:
        raise ValidationError(
            "Разрешение изображения должно быть не меньше 2560х1440 пикселей."
        )


class ShopHeaderImage(models.Model):
    image = models.ImageField(
        upload_to="shop_header_images/", validators=[validate_image]
    )

    def __str__(self) -> str:
        return "Header Image"
