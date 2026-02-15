from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = (
        ("ADMIN", "Admin"),
        ("AUTHOR", "Author"),
        ("STUDENT", "Student"),
    )

    LEVEL_CHOICES = (
        ("Beginner", "Beginner"),
        ("Rising Author", "Rising Author"),
        ("Trusted Author", "Trusted Author"),
        ("Expert Author", "Expert Author"),
    )

    BADGE_CHOICES = (
        ("New Author", "New Author"),
        ("Verified Contributor", "Verified Contributor"),
        ("Top Educator", "Top Educator"),
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

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
        default="Beginner"
    )

    badge = models.CharField(
        max_length=30,
        choices=BADGE_CHOICES,
        default="New Author"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_level_and_badge(self):
        if self.credits <= 20:
            self.level = "Beginner"
            self.badge = "New Author"
        elif self.credits <= 50:
            self.level = "Rising Author"
            self.badge = "Verified Contributor"
        elif self.credits <= 80:
            self.level = "Trusted Author"
            self.badge = "Verified Contributor"
        else:
            self.level = "Expert Author"
            self.badge = "Top Educator"

    def save(self, *args, **kwargs):
        # Safety
        if self.credits < 0:
            self.credits = 0
        if self.credits > 100:
            self.credits = 100

        self.calculate_level_and_badge()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} | {self.level} | {self.credits}"
