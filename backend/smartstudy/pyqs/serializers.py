from rest_framework import serializers
from .models import PYQ
from attempts.models import PYQAttempt


class PYQListSerializer(serializers.ModelSerializer):
    is_attempted = serializers.SerializerMethodField()

    class Meta:
        model = PYQ
        fields = ["id", "title", "subject", "year", "is_attempted"]

    def get_is_attempted(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return PYQAttempt.objects.filter(
                user=request.user,
                pyq=obj
            ).exists()
        return False
