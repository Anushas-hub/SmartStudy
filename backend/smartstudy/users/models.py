from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("AUTHOR", "Author"),
        ("STUDENT", "Student"),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default="STUDENT"
    )
    credits = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_credits(self, amount):
        self.credits = min(100, self.credits + amount)
        self.save()

    @property
    def level(self):
        if self.credits <= 25:
            return "Beginner"
        elif self.credits <= 50:
            return "Intermediate"
        elif self.credits <= 75:
            return "Advanced"
        return "Expert"

    @property
    def badge(self):
        return {
            "Beginner": "🌱 Starter",
            "Intermediate": "📘 Learner",
            "Advanced": "🚀 Achiever",
            "Expert": "🏆 Master",
        }[self.level]

    def __str__(self):
        return f"{self.user.username} ({self.role})"
