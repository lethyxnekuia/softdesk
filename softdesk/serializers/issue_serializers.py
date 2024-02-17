from rest_framework.serializers import ModelSerializer
from softdesk.models import Issue


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        read_only_fields = ['author', 'created_time']
