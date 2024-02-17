from rest_framework.serializers import ModelSerializer
from softdesk.models import Comment
from softdesk.models import Issue
from rest_framework.exceptions import PermissionDenied


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'created_time']

    def perform_create(self, serializer):
        author = self.request.user
        issue_id = self.request.data.get("issue", None)
        try:
            Issue.objects.get(id=issue_id)
        except Issue.DoesNotExist:
            raise PermissionDenied("Issue associée n'existe pas.")
        serializer.save(author=author)
