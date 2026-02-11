from django.urls import path
from .views import PYQListView

urlpatterns = [
    path("", PYQListView.as_view(), name="pyq-list"),
]
