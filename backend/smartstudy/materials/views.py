from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from django.http import FileResponse, Http404

from .models import StudyMaterial
from .serializers import StudyMaterialSerializer
from users.permissions import IsAdminUserRole, IsAuthorRole


# 🌍 PUBLIC LIST (like W3)
class StudyMaterialListView(ListAPIView):
    serializer_class = StudyMaterialSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status']
    ordering_fields = ['uploaded_at']
    ordering = ['-uploaded_at']
    permission_classes = []  # Public access

    def get_queryset(self):
        user = self.request.user

        # Anonymous users → only approved
        if not user.is_authenticated:
            return StudyMaterial.objects.filter(status="APPROVED")

        # Admin → see everything
        if user.profile.role == "ADMIN":
            return StudyMaterial.objects.all()

        # Others → approved only
        return StudyMaterial.objects.filter(status="APPROVED")


# ✍ AUTHOR UPLOAD
class StudyMaterialCreateView(CreateAPIView):
    serializer_class = StudyMaterialSerializer
    permission_classes = [IsAuthorRole]

    def perform_create(self, serializer):
        user = self.request.user

        # Admin upload auto-approved
        if user.profile.role == "ADMIN":
            serializer.save(uploaded_by=user, status="APPROVED")
        else:
            serializer.save(uploaded_by=user, status="PENDING")


# 🛠 ADMIN APPROVAL
class StudyMaterialApproveView(UpdateAPIView):
    queryset = StudyMaterial.objects.all()
    serializer_class = StudyMaterialSerializer
    permission_classes = [IsAdminUserRole]

    def patch(self, request, *args, **kwargs):
        material = self.get_object()
        material.status = request.data.get("status", "APPROVED")
        material.rejection_reason = request.data.get("rejection_reason", "")
        material.save()

        return Response({"message": "Material status updated successfully"})


# 🔐 SECURE DOWNLOAD (Login Required)
class SecureMaterialDownloadView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            material = StudyMaterial.objects.get(pk=pk)
        except StudyMaterial.DoesNotExist:
            raise Http404

        if material.status != "APPROVED":
            return Response({"error": "Material not approved"}, status=403)

        return FileResponse(
            material.file.open(),
            as_attachment=True,
            filename=material.file.name.split("/")[-1]
        )