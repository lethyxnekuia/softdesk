from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from softdesk.models import Project
from softdesk.serializers import ProjectSerializer
from softdesk.permissions import ProjectPermission


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ProjectPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
