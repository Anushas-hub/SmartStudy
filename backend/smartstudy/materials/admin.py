from django.contrib import admin
from .models import StudyMaterial


@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_by', 'status', 'uploaded_at')
    list_filter = ('status', 'uploaded_at')
    search_fields = ('title', 'uploaded_by__username')
    ordering = ('-uploaded_at',)