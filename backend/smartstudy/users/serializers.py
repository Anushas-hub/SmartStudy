from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    level = serializers.ReadOnlyField()
    badge = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ["role", "credits", "level", "badge"]


class SignupSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        default="STUDENT"
    )

    class Meta:
        model = User
        fields = ["username", "password", "email", "role"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        role = validated_data.pop("role")
        user = User.objects.create_user(**validated_data)
        user.profile.role = role
        user.profile.save()
        return user


class UserMeSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ["username", "email", "profile"]
