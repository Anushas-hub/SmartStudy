from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import StudyMaterial
from .serializers import StudyMaterialSerializer


class StudyMaterialListView(ListAPIView):
    serializer_class = StudyMaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = StudyMaterial.objects.all().order_by("-uploaded_at")

        topic_id = self.request.query_params.get("topic")
        if topic_id:
            queryset = queryset.filter(topic_id=topic_id)

        return queryset
