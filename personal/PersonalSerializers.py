from rest_framework import serializers

from login.models import Users


class PersonalSerializer(serializers.Serializer):
    class Meta:
        model = Users
        fields = '__all__'