from rest_framework import serializers
from .models import StudyMaterial


class StudyMaterialSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source="topic.name", read_only=True)

    class Meta:
        model = StudyMaterial
        fields = [
            "id",
            "title",
            "topic",
            "topic_name",
            "file",
            "uploaded_at",
        ]
