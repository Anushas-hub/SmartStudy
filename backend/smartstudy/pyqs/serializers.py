from rest_framework import serializers
from .models import PreviousYearQuestion

class PreviousYearQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreviousYearQuestion
        fields = "__all__"
