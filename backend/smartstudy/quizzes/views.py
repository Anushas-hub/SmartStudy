from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Quiz
from .serializers import QuizSerializer
from .permissions import IsAdminOrAuthor


class QuizCreateAPIView(generics.CreateAPIView):
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated, IsAdminOrAuthor]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class PublicQuizListAPIView(generics.ListAPIView):
    queryset = Quiz.objects.filter(is_published=True)
    serializer_class = QuizSerializer
