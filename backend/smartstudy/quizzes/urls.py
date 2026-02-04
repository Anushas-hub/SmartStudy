from django.urls import path
from .views import QuizDetailAPIView, SubmitQuizAPIView

urlpatterns = [
    path("<int:quiz_id>/", QuizDetailAPIView.as_view()),
    path("<int:quiz_id>/submit/", SubmitQuizAPIView.as_view()),
]
