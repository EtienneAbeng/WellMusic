from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

# Custom user manager extending BaseUserManager
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        """Create and return a regular user with the given username, email, and password."""
        if not username:
            raise ValueError(_('The Username must be set'))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        """Create and return a superuser with the given username, email, password, and other fields."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, email, password, **extra_fields)

# Custom user model extending AbstractUser with additional fields
class CustomUser(AbstractUser):
    """Custom user model extending AbstractUser with additional fields."""
    age = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()  # Using the custom user manager for managing objects

    def __str__(self):
        return self.username  # String representation of the object (username)

# Model for storing music files
class Music(models.Model):
    """Model for storing music files."""
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='music/')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Relationship to the user who uploaded it
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Date and time of upload

    def __str__(self):
        return self.title  # String representation of the object (title of the music)
