from django.urls import path
from .views import (
    ApprovedStudyMaterialList,
    UploadStudyMaterialAPIView,
    MyUploadedMaterialsAPIView,
    SecureMaterialDownloadAPIView,
)

urlpatterns = [
    path("", ApprovedStudyMaterialList.as_view()),
    path("upload/", UploadStudyMaterialAPIView.as_view()),
    path("my/", MyUploadedMaterialsAPIView.as_view()),
    path("<int:pk>/download/", SecureMaterialDownloadAPIView.as_view()),
]
