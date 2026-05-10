from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        FRONTDESK = "FRONTDESK", "Frontdesk"
        STUDENT = "STUDENT", "Student"

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices)

    # optional: only for staff/students under branches
    branch = models.ForeignKey(
        "branches.Branch",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )

    username = None  # we remove username completely

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []