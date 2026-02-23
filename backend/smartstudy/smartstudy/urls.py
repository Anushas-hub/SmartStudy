from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/users/", include("users.urls")),
    path("api/materials/", include("materials.urls")),
    path("api/quizzes/", include("quizzes.urls")),
    path("api/topics/", include("topics.urls")),
    path("api/pyqs/", include("pyqs.urls")),
    path("api/attempts/", include("attempts.urls")),
    path("api/feedback/", include("feedback.urls")),
]