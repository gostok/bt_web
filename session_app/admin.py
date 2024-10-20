from django.contrib import admin
from .models import *

class AvailableTimeInline(admin.TabularInline):
    model = AvailableTime
    extra = 4

class AvailableDateAdmin(admin.ModelAdmin):
    inlines = [AvailableTimeInline]

class SessionAdmin(admin.ModelAdmin):
    list_display = ['date', 'time', 'name', 'contact_info']
    search_fields = ['name', 'date']

admin.site.register(Session, SessionAdmin)
admin.site.register(AvailableDate, AvailableDateAdmin)
