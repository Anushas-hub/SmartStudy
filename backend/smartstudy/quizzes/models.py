from django.db import models
from django.contrib.auth import get_user_model
from topics.models import Topic

User = get_user_model()


class Quiz(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="quizzes"
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_quizzes"
    )

    # admin + author both can create, but publish control stays here
    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


class Question(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="questions"
    )

    question_text = models.TextField()

    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)

    # 🔥 FIXED: default added so migration loop never happens again
    correct_option = models.CharField(
        max_length=1,
        choices=(
            ("A", "A"),
            ("B", "B"),
            ("C", "C"),
            ("D", "D"),
        ),
        default="A",
    )

    marks = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quiz.title} - {self.question_text[:40]}"


class QuizAttempt(models.Model):
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.CASCADE,
        related_name="attempts"
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="quiz_attempts"
    )

    score = models.PositiveIntegerField(default=0)
    total_marks = models.PositiveIntegerField(default=0)

    attempted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-attempted_at"]

    def __str__(self):
        return f"{self.student} - {self.quiz}"
