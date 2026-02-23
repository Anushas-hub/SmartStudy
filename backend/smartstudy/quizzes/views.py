from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer


# Admin → Create & List
class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [IsAuthenticated]


# Public → Only Published Quizzes
class PublicQuizListView(generics.ListAPIView):
    queryset = Quiz.objects.filter(is_published=True)
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]


@api_view(['POST'])
def publish_quiz(request, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
        quiz.is_published = True
        quiz.save()
        return Response({"message": "Quiz published successfully"})
    except Quiz.DoesNotExist:
        return Response({"error": "Quiz not found"}, status=404)


@api_view(['POST'])
def add_question(request, pk):
    try:
        quiz = Quiz.objects.get(pk=pk)
        data = request.data
        data['quiz'] = quiz.id
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    except Quiz.DoesNotExist:
        return Response({"error": "Quiz not found"}, status=404)