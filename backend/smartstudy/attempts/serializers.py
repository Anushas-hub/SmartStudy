from rest_framework import serializers
from .models import QuizAttempt


class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = '__all__'
        read_only_fields = ('user', 'score', 'status', 'started_at', 'completed_at')