from django.db import models
from core.models import TimeStampedModel


class Document(TimeStampedModel):
    application = models.ForeignKey(
        "applications.Application",
        on_delete=models.CASCADE,
        related_name="documents"
    )

    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.title