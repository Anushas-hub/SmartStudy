from rest_framework import serializers
from .models import PYQAttempt


class PYQAttemptCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PYQAttempt
        fields = ["pyq"]


class PYQAttemptSerializer(serializers.ModelSerializer):
    pyq_title = serializers.CharField(source="pyq.title", read_only=True)
    year = serializers.IntegerField(source="pyq.year", read_only=True)

    class Meta:
        model = PYQAttempt
        fields = ["id", "pyq", "pyq_title", "year", "attempted_at"]
