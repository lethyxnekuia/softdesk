import uuid
from django.db import models
from .issue import Issue
from django.conf import settings


class Comment(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="created_comments",
        on_delete=models.CASCADE,
    )
    issue = models.ForeignKey(
        to=Issue,
        related_name="issue_comments",
        on_delete=models.CASCADE,
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
