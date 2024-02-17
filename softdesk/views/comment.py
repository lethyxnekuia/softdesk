from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from softdesk.models import Comment
from softdesk.serializers import CommentSerializer
from softdesk.permissions import CommentPermission, IsAuthorPermission


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorPermission, CommentPermission]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
