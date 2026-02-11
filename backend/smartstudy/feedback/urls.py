from django.urls import path
from .views import FeedbackCreateView, MyFeedbackListView

urlpatterns = [
    path("create/", FeedbackCreateView.as_view(), name="feedback-create"),
    path("my/", MyFeedbackListView.as_view(), name="my-feedback"),
]
