from django.contrib import admin

from technicians.models import TechnicianModel


@admin.register(TechnicianModel)
class TechnicianAdmin(admin.ModelAdmin):
    pass
