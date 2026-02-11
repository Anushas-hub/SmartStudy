from django.db import models
from django.conf import settings
from pyqs.models import PYQ


class PYQAttempt(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    pyq = models.ForeignKey(
        PYQ,
        on_delete=models.CASCADE,
        related_name="attempts"
    )
    attempted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "pyq")

    def __str__(self):
        return f"{self.user} attempted {self.pyq}"
