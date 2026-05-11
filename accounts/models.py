from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


# -------------------
# CUSTOM USER MANAGER
# -------------------
class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("role", "ADMIN")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


# -------------------
# USER MODEL
# -------------------
class User(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        FRONTDESK = "FRONTDESK", "Frontdesk"
        STUDENT = "STUDENT", "Student"

    username = None  # remove username completely

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=Role.choices)

    branch = models.ForeignKey(
        "branches.Branch",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="users"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()