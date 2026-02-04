import os
from django.http import FileResponse, Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import generics

from .models import StudyMaterial
from .serializers import (
    StudyMaterialSerializer,
    StudyMaterialUploadSerializer,
)
from users.models import Profile


# 🎓 Students: ONLY approved materials
class ApprovedStudyMaterialList(generics.ListAPIView):
    serializer_class = StudyMaterialSerializer

    def get_queryset(self):
        return StudyMaterial.objects.filter(status="APPROVED")


# ⬆️ Upload (AUTHOR / ADMIN)
class UploadStudyMaterialAPIView(generics.CreateAPIView):
    serializer_class = StudyMaterialUploadSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)

        if profile.role not in ["AUTHOR", "ADMIN"]:
            raise PermissionError("Not allowed")

        serializer.save(
            uploaded_by=self.request.user,
            status="PENDING",
        )


# 📂 My uploads
class MyUploadedMaterialsAPIView(generics.ListAPIView):
    serializer_class = StudyMaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return StudyMaterial.objects.filter(
            uploaded_by=self.request.user
        )


# 🔐 Secure download
class SecureMaterialDownloadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            material = StudyMaterial.objects.get(pk=pk)
        except StudyMaterial.DoesNotExist:
            raise Http404("Material not found")

        if material.status != "APPROVED":
            if (
                material.uploaded_by != request.user
                and not request.user.is_staff
            ):
                return Response(
                    {"detail": "Access denied"},
                    status=403,
                )

        return FileResponse(
            open(material.file.path, "rb"),
            as_attachment=True,
            filename=os.path.basename(material.file.name),
        )