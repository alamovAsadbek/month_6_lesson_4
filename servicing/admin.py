from django.contrib import admin

from servicing.models import ServiceModel


@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'name', 'price', 'description', 'created_at')
    list_display_links = ('id', 'description', 'name', 'price', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('description', 'name', 'price')
    list_per_page = 10
