from datetime import datetime

from django.db import models

class Project(models.Model):
    """Project model"""
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    icon = models.ImageField(upload_to='project_icons/', null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    technology_stack = models.ManyToManyField("TechnologyName", blank=True)
    is_published = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TechnologyName(models.Model):
    """Technology name model"""
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.ImageField(upload_to='technology_icons/', null=True, blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name