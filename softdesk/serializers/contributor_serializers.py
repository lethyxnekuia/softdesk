from rest_framework.serializers import ModelSerializer
from softdesk.models import Contributor


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = '__all__'
