from django.contrib import admin
from .models import PYQ

@admin.register(PYQ)
class PYQAdmin(admin.ModelAdmin):
    list_display = ("title", "subject", "year", "exam_type")
    list_filter = ("year", "exam_type", "subject")
