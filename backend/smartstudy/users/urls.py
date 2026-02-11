from django.urls import path
from .views import MyCreditsAPIView, SignupAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path("signup/", SignupAPIView.as_view()),
    path("login/", LoginAPIView.as_view()),
    path("logout/", LogoutAPIView.as_view()),
    path("my-credits/", MyCreditsAPIView.as_view()),
]
