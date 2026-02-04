from django.db import models
from django.contrib.auth import get_user_model
from topics.models import Topic

User = get_user_model()


class StudyMaterial(models.Model):
    # 🔗 Link to Topic (safe unlink if topic deleted)
    topic = models.ForeignKey(
        Topic,
        on_delete=models.SET_NULL,
        related_name="materials",
        null=True,
        blank=True,
    )

    subject = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    # 📄 Only files (PDF restriction handled elsewhere)
    file = models.FileField(upload_to="materials/")

    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="uploaded_materials",
    )

    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    rejection_reason = models.TextField(blank=True, null=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title
