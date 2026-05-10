from django.db import models
from core.models import TimeStampedModel


class FollowUp(TimeStampedModel):
    application = models.ForeignKey(
        "applications.Application",
        on_delete=models.CASCADE,
        related_name="followups"
    )

    handled_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    note = models.TextField()
    next_action_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"FollowUp - {self.application.id}"