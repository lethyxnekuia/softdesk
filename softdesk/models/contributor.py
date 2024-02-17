from django.db import models
from .project import Project
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Contributor(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="contributors",
        on_delete=models.CASCADE,
    )
    project = models.ForeignKey(
        to=Project, related_name="projects", on_delete=models.CASCADE, blank=True
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

    @receiver(post_save, sender=Project)
    def create_author_contributor(sender, instance, created, **kwargs):
        if created:
            Contributor.objects.create(
                user=instance.author, project=instance
            )
