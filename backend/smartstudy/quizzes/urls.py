from django.urls import path
from .views import (
    QuizListCreateView,
    PublicQuizListView,
    publish_quiz,
    add_question
)

urlpatterns = [
    path('', QuizListCreateView.as_view(), name='quiz-list-create'),
    path('public/', PublicQuizListView.as_view(), name='quiz-public-list'),
    path('<int:pk>/publish/', publish_quiz, name='quiz-publish'),
    path('<int:pk>/add-question/', add_question, name='quiz-add-question'),
]