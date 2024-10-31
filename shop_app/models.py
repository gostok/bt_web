from django.db import models
from django.core.exceptions import ValidationError
from home_app.models import SidebarNews, HeaderImage


class ShopSidebarNews(SidebarNews):
    pass


class ShopHeaderImage(HeaderImage):
    pass


class Seller(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    CONTACT_TYPE_CHOICES = [
        ("Телефон", "Телефон"),
        ("Email", "Email"),
        ("Соц-сеть", "Соц-сеть"),
    ]
    seller = models.ForeignKey(
        Seller, related_name="contacts", on_delete=models.CASCADE
    )
    contact_type = models.CharField(max_length=100, choices=CONTACT_TYPE_CHOICES)
    value = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.get_contact_type_display()}: {self.value}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    description = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.seller}: {self.title}"

    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * (1 - self.discount / 100)
        return self.price


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="product_images/")

    def __str__(self) -> str:
        return f"Image for {self.product.title}"
