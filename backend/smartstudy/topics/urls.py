from django.urls import path
from .views import PublicTopicListAPIView, PublicTopicDetailAPIView

urlpatterns = [
    path("", PublicTopicListAPIView.as_view(), name="topic-list"),
    path("<slug:slug>/", PublicTopicDetailAPIView.as_view(), name="topic-detail"),
]
