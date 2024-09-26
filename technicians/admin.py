from django.contrib import admin

from technicians.models import TechnicianModel


@admin.register(TechnicianModel)
class TechnicianAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone_number', 'address']
