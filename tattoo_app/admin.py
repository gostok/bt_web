from django.contrib import admin
from .models import *


class TattooImageInline(admin.TabularInline):
    model = TattooImage
    extra = 1


class MasterImageInline(admin.TabularInline):
    model = MasterImage
    extra = 1


class TattooAdmin(admin.ModelAdmin):
    change_form_template = "admin/Tattoo_change_form.html"
    list_display = ("title", "publication_date", "category")
    search_fields = ("title",)
    list_filter = ("publication_date", "category")
    inlines = [TattooImageInline]


class MasterAdmin(admin.ModelAdmin):
    change_form_template = "admin/Master_change_form.html"
    list_display = ("name", "publication_date", "category")
    search_fields = ("name",)
    list_filter = ("publication_date", "category")
    inlines = [MasterImageInline]


admin.site.register(Category)
admin.site.register(Tattoo, TattooAdmin)
admin.site.register(Master, MasterAdmin)
