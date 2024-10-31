from django.contrib import admin
from django.utils.html import format_html
from .models import *


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    prepopulated_fields = {"short_description": ("title",)}


class SidebarNewsAdmin(admin.ModelAdmin):
    list_display = ("title",)


class HeaderImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image")

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Добавляем подсказку в форму
        form.base_fields["image"].help_text = format_html(
            '<div style="color: red; font-weight: bold;">'
            "Пожалуйста, загрузите изображение размером не меньше 2560х1440 пикселей."
            "</div>"
        )
        return form


@admin.register(SiteStatistics)
class SiteStatisticsAdmin(admin.ModelAdmin):
    list_display = ("total_visits",)


admin.site.register(CarouselImage)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(SidebarNews, SidebarNewsAdmin)
admin.site.register(HeaderImage, HeaderImageAdmin)
