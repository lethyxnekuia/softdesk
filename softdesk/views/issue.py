from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from softdesk.models import Issue, Contributor
from softdesk.serializers import IssueSerializer
from softdesk.permissions import IssuePermission, IsAuthorPermission


class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated, IsAuthorPermission, IssuePermission]

    def perform_create(self, serializer):
        author = self.request.user
        project_id = self.request.data.get("project")
        if not Contributor.objects.filter(user__pk=author.id, project__pk=project_id).exists():
            raise PermissionDenied("Seuls les contributeurs du projet peuvent créer un problème.")

        assignee_id = self.request.data.get("assigned_to", None)
        if assignee_id:
            is_contributor = Contributor.objects.filter(
                user__pk=assignee_id, project__pk=project_id
            ).exists()
            if not is_contributor:
                raise PermissionDenied("L'utilisateur assigné doit être un contributeur du projet.")
        serializer.save(author=author)
