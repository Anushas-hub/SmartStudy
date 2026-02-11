from django.db import models
from django.conf import settings
from pyqs.models import PreviousYearQuestion

class PYQAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pyq = models.ForeignKey(PreviousYearQuestion, on_delete=models.CASCADE)
    attempted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "pyq")

    def __str__(self):
        return f"{self.user} attempted {self.pyq}"
