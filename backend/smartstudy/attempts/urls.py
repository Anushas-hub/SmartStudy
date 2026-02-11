from django.urls import path
from .views import PYQAttemptCreateView, MyAttemptsListView

urlpatterns = [
    path("attempt/", PYQAttemptCreateView.as_view()),
    path("my-attempts/", MyAttemptsListView.as_view()),
]
