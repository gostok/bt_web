from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 8


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ["title", "price", "discount"]
    fields = ["title", "price", "discount", "description", "seller"]


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 6


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_display = ["name"]


admin.site.register(Product, ProductAdmin)
