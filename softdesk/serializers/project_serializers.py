from rest_framework.serializers import ModelSerializer
from softdesk.models import Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['author', 'created_time']
