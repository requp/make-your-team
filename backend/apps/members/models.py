from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator

class BaseMemberManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        if not password:
            raise ValueError("The Password field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(
            email=email, password=password, username=username, **extra_fields
        )


class Member(AbstractUser):
    """Model for Members"""
    username = models.CharField(validators=[MinLengthValidator(4)], max_length=32, unique=True)
    email=models.EmailField(max_length=254, unique=True)
    profile_pic = models.ImageField(upload_to="member_pics/", blank=True, null=True)
    phone_number = models.CharField(blank=True, null=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    skills = models.ManyToManyField("Skill", blank=True)
    is_verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = BaseMemberManager()

    def __str__(self):
        return f"{self.username}-{self.email}"

    def save(self, *args, **kwargs):
        #TODO Until adding email verification
        if not self.pk:
            self.is_verified = True
        return super().save(*args, **kwargs)


class Skill(models.Model):
    """Model for Skills"""
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="skill_icons/", blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
