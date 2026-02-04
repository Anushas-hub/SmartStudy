from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Quiz, Choice, QuizAttempt
from .serializers import QuizSerializer


class QuizDetailAPIView(APIView):
    def get(self, request, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id, is_active=True)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)


class SubmitQuizAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id)
        answers = request.data.get("answers", {})

        score = 0
        total = quiz.questions.count()

        for question in quiz.questions.all():
            selected_choice_id = answers.get(str(question.id))
            if selected_choice_id:
                if Choice.objects.filter(
                    id=selected_choice_id,
                    question=question,
                    is_correct=True
                ).exists():
                    score += 1

        QuizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=score,
            total_questions=total,
        )

        return Response({
            "score": score,
            "total": total
        })
