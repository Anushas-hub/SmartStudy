from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

from quizzes.models import Quiz
from .models import QuizAttempt, UserAnswer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_or_resume_quiz(request, quiz_id):
    quiz = Quiz.objects.filter(id=quiz_id, is_published=True).first()
    if not quiz:
        return Response({"error": "Quiz not found"}, status=404)

    attempt, created = QuizAttempt.objects.get_or_create(
        user=request.user,
        quiz=quiz,
        defaults={'status': 'in_progress'}
    )

    if attempt.status == 'completed':
        return Response({"error": "Quiz already completed"}, status=400)

    return Response({
        "attempt_id": attempt.id,
        "started_at": attempt.started_at,
        "time_limit": quiz.time_limit
    })


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_quiz(request, quiz_id):
    attempt = QuizAttempt.objects.filter(
        user=request.user,
        quiz_id=quiz_id,
        status='in_progress'
    ).first()

    if not attempt:
        return Response({"error": "No active attempt"}, status=400)

    quiz = attempt.quiz

    # Timer validation
    time_elapsed = timezone.now() - attempt.started_at
    if time_elapsed > timedelta(minutes=quiz.time_limit):
        return Response({"error": "Time expired"}, status=400)

    answers = request.data.get("answers", {})
    score = 0

    for question in quiz.questions.all():
        selected = answers.get(str(question.id))
        if not selected:
            continue

        is_correct = selected == question.correct_answer

        if is_correct:
            score += 1
        else:
            score -= quiz.negative_marking

        UserAnswer.objects.create(
            attempt=attempt,
            question=question,
            selected_option=selected,
            is_correct=is_correct
        )

    attempt.score = score
    attempt.status = 'completed'
    attempt.completed_at = timezone.now()
    attempt.save()

    return Response({"score": score})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def leaderboard(request, quiz_id):
    attempts = QuizAttempt.objects.filter(
        quiz_id=quiz_id,
        status='completed'
    ).order_by('-score')

    ranked = []
    for index, attempt in enumerate(attempts, start=1):
        ranked.append({
            "rank": index,
            "username": attempt.user.username,
            "score": attempt.score
        })

    return Response(ranked)