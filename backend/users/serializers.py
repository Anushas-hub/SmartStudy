from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
