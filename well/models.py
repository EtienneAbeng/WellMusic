from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """Create and return a regular user with the given username and password."""
        if not username:
            raise ValueError(_('The Username must be set'))

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """Create and return a superuser with the given username, password, and other fields."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom user model extending AbstractUser with additional fields."""
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
