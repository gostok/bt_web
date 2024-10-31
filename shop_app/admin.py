from django.contrib import admin
from django.utils.html import format_html
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "discount"]
    fields = ["title", "price", "discount", "description", "seller"]
    inlines = [ProductImageInline]


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    list_display = ["name"]


admin.site.register(Product, ProductAdmin)
