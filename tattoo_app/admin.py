from django.contrib import admin
from .models import *

class TattooAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date')
    search_fields = ('title',)
    list_filter = ('publication_date',)

class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'publication_date')
    search_fields = ('name',)
    list_filter = ('publication_date',)

admin.site.register(Tattoo, TattooAdmin)
admin.site.register(Master, MasterAdmin)