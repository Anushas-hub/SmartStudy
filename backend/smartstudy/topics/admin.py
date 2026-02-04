from django.contrib import admin
from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("title", "is_public", "created_at")
    list_filter = ("is_public",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("title",)