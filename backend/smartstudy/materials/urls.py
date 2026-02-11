from django.urls import path
from .views import StudyMaterialListView

urlpatterns = [
    path("", StudyMaterialListView.as_view(), name="material-list"),
]
