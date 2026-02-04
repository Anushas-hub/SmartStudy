from django.contrib import admin
from .models import StudyMaterial


@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "topic",
        "uploaded_by",
        "status",
        "uploaded_at",
    )

    list_filter = ("status", "topic")
    search_fields = ("title", "subject")
    ordering = ("-uploaded_at",)

    readonly_fields = ("uploaded_by", "uploaded_at")

    fields = (
        "title",
        "subject",
        "description",
        "file",
        "topic",
        "uploaded_by",
        "status",
        "rejection_reason",
        "uploaded_at",
    )

    actions = ["approve_materials", "reject_materials"]

    # ✅ Auto-set uploader (admin upload case)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)

    # ✅ Approve materials
    def approve_materials(self, request, queryset):
        queryset.update(status="APPROVED", rejection_reason=None)

    approve_materials.short_description = "Approve selected materials"

    # ❌ Reject materials (reason can be added manually)
    def reject_materials(self, request, queryset):
        queryset.update(status="REJECTED")

    reject_materials.short_description = "Reject selected materials"
