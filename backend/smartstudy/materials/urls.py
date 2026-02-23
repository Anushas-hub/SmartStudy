from django.urls import path
from .views import (
    StudyMaterialListView,
    StudyMaterialCreateView,
    StudyMaterialApproveView,
    SecureMaterialDownloadView
)

urlpatterns = [
    path('', StudyMaterialListView.as_view()),
    path('upload/', StudyMaterialCreateView.as_view()),
    path('approve/<int:pk>/', StudyMaterialApproveView.as_view()),
    path('download/<int:pk>/', SecureMaterialDownloadView.as_view()),
]