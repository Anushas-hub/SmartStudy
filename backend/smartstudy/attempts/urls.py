from django.urls import path
from .views import PYQAttemptCreateView, MyAttemptsListView

urlpatterns = [
    path("attempt/", PYQAttemptCreateView.as_view(), name="pyq-attempt"),
    path("my-attempts/", MyAttemptsListView.as_view(), name="my-attempts"),
]
