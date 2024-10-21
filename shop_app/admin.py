from django.contrib import admin
from .models import *


class ShopHeaderImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")


admin.site.register(ShopHeaderImage, ShopHeaderImageAdmin)
