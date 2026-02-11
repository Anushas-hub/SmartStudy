from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError

from .models import PYQAttempt
from .serializers import PYQAttemptSerializer, PYQAttemptCreateSerializer


class PYQAttemptCreateView(CreateAPIView):
    """
    Create PYQ Attempt
    - User must be authenticated
    - Same user cannot attempt same PYQ twice
    """
    queryset = PYQAttempt.objects.all()
    serializer_class = PYQAttemptCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        pyq = serializer.validated_data["pyq"]

        # 🔒 Prevent duplicate attempts
        if PYQAttempt.objects.filter(user=user, pyq=pyq).exists():
            raise ValidationError({
                "detail": "You have already attempted this PYQ."
            })

        serializer.save(user=user)


class MyAttemptsListView(ListAPIView):
    """
    List all attempts of logged-in user
    """
    serializer_class = PYQAttemptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return PYQAttempt.objects.filter(user=self.request.user).order_by("-attempted_at")
