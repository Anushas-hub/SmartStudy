from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    RATING_CHOICES = [
        (1, "Very Bad"),
        (2, "Bad"),
        (3, "Average"),
        (4, "Good"),
        (5, "Excellent"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="feedbacks"
    )
    rating = models.IntegerField(choices=RATING_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}"
