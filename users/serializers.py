from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import User


class UserSerializer(ModelSerializer):
    age = serializers.IntegerField(write_only=True)

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'password',
                  'age',
                  'can_be_contacted',
                  'can_be_shared']

    def create(self, validated_data):
        if validated_data['age'] < 15:
            raise serializers.ValidationError("Vous devez avoir au moins 15 ans.")
        else:
            del validated_data['age']
            return User.objects.create_user(**validated_data)
