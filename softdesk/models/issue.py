from django.db import models
from django.conf import settings
from .project import Project
from .contributor import Contributor
from .choices import TagChoice, PriorityChoice, StatusChoice


class Issue(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    tag = models.CharField(max_length=48, blank=True, null=True, choices=TagChoice.get_as_choices())
    priority = models.CharField(max_length=48, blank=True, null=True, choices=PriorityChoice.get_as_choices())
    status = models.CharField(max_length=48, default=StatusChoice.TO_DO, choices=StatusChoice.get_as_choices())
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="created_issues",
        on_delete=models.CASCADE,
    )
    project = models.ForeignKey(
        to=Project,
        related_name="project_issues",
        on_delete=models.CASCADE,
    )
    assigned_to = models.ForeignKey(
        to=Contributor,
        related_name="assigned_issues",
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(auto_now_add=True)
