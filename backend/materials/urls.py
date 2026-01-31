from django.urls import path
from .views import material_list, upload_material

urlpatterns = [
    path('materials/', material_list),
    path('materials/upload/', upload_material),
]
