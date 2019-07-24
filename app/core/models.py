from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

# Create your models here.


class UserManager(BaseUserManager):
    """custom user Manager"""

    def create_user(self, email, password=None, **extra_fields):
        """Creates a user"""
        if not email:
            raise ValueError('A Username is required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    """User Profile"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    age = models.IntegerField()
    bio = models.TextField(blank=True, null=True)
    is_writer = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name
