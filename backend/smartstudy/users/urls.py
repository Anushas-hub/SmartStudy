from django.urls import path
from .views import login_user, current_user

urlpatterns = [
    path('login/', login_user),
    path('me/', current_user),
]
