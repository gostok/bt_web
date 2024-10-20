from django.contrib import admin
from .models import *


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    prepopulated_fields = {'short_description': ('title',)}


class SidebarNewsAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(CarouselImage)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(SidebarNews, SidebarNewsAdmin)