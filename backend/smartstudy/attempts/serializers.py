from rest_framework import serializers
from .models import PYQAttempt

class PYQAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = PYQAttempt
        fields = "__all__"
        read_only_fields = ("user",)
