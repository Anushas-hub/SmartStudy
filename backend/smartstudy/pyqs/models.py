from django.db import models
from topics.models import Topic


def year_choices():
    return [(y, y) for y in range(2015, 2031)]


class PYQ(models.Model):
    title = models.CharField(max_length=255)

    subject = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        related_name="pyqs"
    )

    year = models.IntegerField(choices=year_choices())

    exam_type = models.CharField(
        max_length=20,
        choices=[
            ("mid", "Mid Semester"),
            ("end", "End Semester"),
        ]
    )

    paper = models.FileField(upload_to="pyqs/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.year} ({self.exam_type})"
