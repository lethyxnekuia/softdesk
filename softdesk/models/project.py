from django.db import models
from .choices import ProjectTypeChoice
from django.conf import settings


class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(max_length=48, choices=ProjectTypeChoice.get_as_choices())
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="created_projects",
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
