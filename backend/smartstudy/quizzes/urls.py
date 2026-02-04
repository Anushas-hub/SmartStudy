from django.urls import path
from .views import QuizCreateAPIView, PublicQuizListAPIView

urlpatterns = [
    path("create/", QuizCreateAPIView.as_view()),
    path("public/", PublicQuizListAPIView.as_view()),
]
