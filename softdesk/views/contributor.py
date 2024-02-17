from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from softdesk.models import Contributor
from softdesk.serializers import ContributorSerializer
from rest_framework.exceptions import PermissionDenied
from softdesk.models import Project
from softdesk.permissions import ContributorPermission, IsAuthorPermission


class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated, IsAuthorPermission, ContributorPermission]

    def perform_create(self, serializer):
        project = self.request.data.get("project")
        if Project.objects.get(id=project).author == self.request.user:
            serializer.save()
        else:
            raise PermissionDenied(
                "Vous devez être l'auteur du projet pour ajouter des contributeurs."
            )
