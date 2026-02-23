from rest_framework import serializers
from .models import StudyMaterial


class StudyMaterialSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.ReadOnlyField(source="uploaded_by.username")

    class Meta:
        model = StudyMaterial
        fields = [
            "id",
            "title",
            "description",
            "file",
            "uploaded_by",
            "status",
            "rejection_reason",
            "uploaded_at",
        ]
        read_only_fields = ["status", "uploaded_by", "uploaded_at"]