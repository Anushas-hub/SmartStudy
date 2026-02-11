from django.contrib import admin
from .models import PYQAttempt

@admin.register(PYQAttempt)
class PYQAttemptAdmin(admin.ModelAdmin):
    list_display = ("user", "pyq", "attempted_at")
