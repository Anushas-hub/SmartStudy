from django.contrib import admin
from .models import PYQ

@admin.register(PYQ)
class PYQAdmin(admin.ModelAdmin):
    list_display = ("title", "year")
    list_filter = ("year",)
    search_fields = ("title",)
