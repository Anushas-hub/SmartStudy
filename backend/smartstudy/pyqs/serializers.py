from rest_framework import serializers
from .models import PYQ


class PYQSerializer(serializers.ModelSerializer):
    class Meta:
        model = PYQ
        fields = "__all__"
