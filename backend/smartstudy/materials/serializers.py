from rest_framework import serializers
from .models import StudyMaterial


class StudyMaterialSerializer(serializers.ModelSerializer):
    topic_title = serializers.CharField(
        source="topic.title", read_only=True
    )

    class Meta:
        model = StudyMaterial
        fields = "__all__"


class StudyMaterialUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = (
            "title",
            "subject",
            "description",
            "file",
            "topic",
        )
