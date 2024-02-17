from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from softdesk.models import Contributor


def is_contributor(user, project):
    if Contributor.objects.filter(user=user, project=project).exists():
        return True
    else:
        raise PermissionDenied(
                    "Seul un contributeur peut effectuer cette action"
                )


class IsAuthorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "DELETE", "PATCH"]:
            if obj.author == request.user:
                return True
            else:
                raise PermissionDenied(
                    "Seul l'auteur peut effectuer cette action"
                )
        return True


class ProjectPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return is_contributor(self.user, obj.project)
        return True


class ContributorPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return is_contributor(self.user, obj.project)


class IssuePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return is_contributor(self.user, obj.project)


class CommentPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return is_contributor(self.user, obj.issue.project)
