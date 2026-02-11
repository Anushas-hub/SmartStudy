from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import PYQ
from .serializers import PYQListSerializer


class PYQListView(ListAPIView):
    queryset = PYQ.objects.all().order_by("-year")
    serializer_class = PYQListSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context
