from django.contrib import admin
from .models import *


class ShopHeaderImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 3


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("seller", "contact_type", "value")


admin.site.register(ShopHeaderImage, ShopHeaderImageAdmin)
admin.site.register(Product, ProductAdmin)
