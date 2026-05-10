from django.db import models
from core.models import TimeStampedModel


class Application(TimeStampedModel):

    class Status(models.TextChoices):
        SUBMITTED = "SUBMITTED", "Submitted"
        UNDER_REVIEW = "UNDER_REVIEW", "Under Review"
        APPROVED = "APPROVED", "Approved"
        REJECTED = "REJECTED", "Rejected"

    student = models.ForeignKey(
        "students.Student",
        on_delete=models.CASCADE,
        related_name="applications"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SUBMITTED
    )

    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.full_name} - {self.status}"