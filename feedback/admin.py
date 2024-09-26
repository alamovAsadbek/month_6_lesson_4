from django.contrib import admin

from feedback.models import FeedbackModel

admin.site.site_header = 'Admin Panel'


@admin.register(FeedbackModel)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user_firstname', 'user_lastname', 'title', 'message', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user_firstname', 'user_lastname', 'title', 'email')
    list_display_links = ('user_firstname', 'user_lastname', 'title', 'message', 'email', 'created_at')
