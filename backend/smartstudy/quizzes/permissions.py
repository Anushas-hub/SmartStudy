from rest_framework.permissions import BasePermission
from users.models import Profile


class IsAdminOrAuthor(BasePermission):
    def has_permission(self, request, view):
        profile = Profile.objects.get(user=request.user)
        return profile.role in ["ADMIN", "AUTHOR"]
