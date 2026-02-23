from django.urls import path
from .views import start_or_resume_quiz, submit_quiz

urlpatterns = [
    path("start/<int:quiz_id>/", start_or_resume_quiz),
    path("submit/<int:quiz_id>/", submit_quiz),
]