from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import PYQAttempt
from .serializers import PYQAttemptSerializer


class PYQAttemptCreateView(CreateAPIView):
    serializer_class = PYQAttemptSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyAttemptsListView(ListAPIView):
    serializer_class = PYQAttemptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PYQAttempt.objects.filter(
            user=self.request.user
        ).select_related("pyq").order_by("-attempted_at")
