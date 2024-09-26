from django.contrib import admin

from technicians.models import TechnicianModel


@admin.register(TechnicianModel)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'created_at']
    list_display_links = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'created_at']
    search_fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']
    readonly_fields = ['id']
    fieldsets = [
        ('Personal Information', {'fields': ['first_name', 'last_name', 'email', 'phone_number', 'address']}),
        ('Technical Information', {'fields': ['id']}),
    ]
    list_per_page = 10
