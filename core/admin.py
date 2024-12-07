from django.contrib import admin

from .models import *


class IPv4GeoDataModelAdmin(admin.ModelAdmin):
    list_display = ['ipv4', 'country', 'province', 'city']
    list_filter = ['country']
    search_fields = ['ipv4', 'country', 'province', 'city']
    ordering = ['ipv4']


admin.site.register(IPv4GeoDataModel, IPv4GeoDataModelAdmin)