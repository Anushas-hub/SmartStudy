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
    search_fields = ("title",)

    readonly_fields = ("uploaded_by", "uploaded_at")

    actions = ["approve_materials", "reject_materials"]

    # 🔹 ADD vs CHANGE form control
    def get_fields(self, request, obj=None):
        """
        ADD form → no status / rejection reason
        CHANGE form → full review controls
        """
        base_fields = [
            "title",
            "subject",
            "description",
            "file",
            "topic",
        ]

        if obj:  # change / review
            return base_fields + [
                "uploaded_by",
                "status",
                "rejection_reason",
                "uploaded_at",
            ]

        return base_fields  # add form

    def save_model(self, request, obj, form, change):
        # Admin upload → auto approved
        if not change:
            obj.uploaded_by = request.user
            obj.status = "APPROVED"
        super().save_model(request, obj, form, change)

    def approve_materials(self, request, queryset):
        queryset.update(status="APPROVED", rejection_reason=None)

    def reject_materials(self, request, queryset):
        queryset.update(status="REJECTED")

    approve_materials.short_description = "Approve selected"
    reject_materials.short_description = "Reject selected"
