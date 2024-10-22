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


class Seller(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    seller = models.ForeignKey(
        Seller, related_name="contacts", on_delete=models.CASCADE
    )
    contact_type = models.CharField(max_length=100)
    value = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.contact_type}: {self.value}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.seller}: {self.title}"


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/")

    def __str__(self) -> str:
        return f"Image for {self.product.title}"
