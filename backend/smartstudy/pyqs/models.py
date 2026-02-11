from django.db import models


class PYQ(models.Model):
    title = models.CharField(max_length=255)
    subject = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.year})"
