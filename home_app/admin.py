from django.contrib import admin
from django.utils.html import format_html
from .models import *


class CarouselImageAdmin(admin.ModelAdmin):

    change_form_template = "admin/Carousel_change_form.html"


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    prepopulated_fields = {"short_description": ("title",)}

    change_form_template = "admin/BlogPost_change_form.html"


class SidebarNewsAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(SiteStatistics)
class SiteStatisticsAdmin(admin.ModelAdmin):
    list_display = ("total_visits",)


admin.site.register(CarouselImage, CarouselImageAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(SidebarNews, SidebarNewsAdmin)
