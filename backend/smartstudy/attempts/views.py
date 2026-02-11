from rest_framework import generics, permissions
from .models import PYQAttempt
from .serializers import PYQAttemptSerializer

class PYQAttemptCreateView(generics.CreateAPIView):
    serializer_class = PYQAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MyAttemptsListView(generics.ListAPIView):
    serializer_class = PYQAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PYQAttempt.objects.filter(user=self.request.user)
