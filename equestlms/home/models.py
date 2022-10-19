import auto_prefetch
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField

from equestlms.utils.choices import GENDER_CHOICES
from equestlms.utils.media import MediaHelper
from equestlms.utils.models import TimeBasedModel


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def create_staff(self, email, password, **extra_fields):
        """Create and save a StaffUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("StaffUser must have is_staff=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(TimeBasedModel, AbstractUser):
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]

    is_new = models.BooleanField(default=True)
    email = models.EmailField(verbose_name="email address", unique=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    profile_pic = ResizedImageField(
        upload_to=MediaHelper.get_image_upload_path,
        blank=True,
        verbose_name="Profile Picture",
        null=True,
    )
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=20, null=True, blank=True
    )

    objects = UserManager()

    class Meta(auto_prefetch.Model.Meta):
        ordering = ["first_name", "last_name"]
        verbose_name = "user"

    def __str__(self):
        return self.get_full_name() or self.email

    @property
    def image_url(self):
        """return image if it exists otherwise use a default"""
        if self.profile_pic:
            return self.profile_pic.url

        return f"{settings.STATIC_URL}img/equest_logo.png"

    def get_absolute_url(self):
        if self.is_staff:
            return reverse("tutor:tutor_dashboard")
        return reverse("home:profile", kwargs={"username": self.username})
