from rest_framework import serializers

from login.models import Users


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'