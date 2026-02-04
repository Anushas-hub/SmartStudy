from rest_framework import serializers
from .models import Topic
from materials.models import StudyMaterial


class TopicMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyMaterial
        fields = (
            "id",
            "title",
            "file",
            "uploaded_at",
        )


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = (
            "id",
            "title",
            "slug",
        )


class TopicDetailSerializer(serializers.ModelSerializer):
    materials = serializers.SerializerMethodField()

    class Meta:
        model = Topic
        fields = (
            "id",
            "title",
            "content",
            "materials",
        )

    def get_materials(self, obj):
        return TopicMaterialSerializer(
            obj.materials.filter(status="APPROVED"),
            many=True,
        ).data
