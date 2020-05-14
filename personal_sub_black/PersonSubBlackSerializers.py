from itsdangerous import serializer

from login.models import Subscriptions, Blacklists


class MyFollowSerializer(serializer.Serializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'


class MyBlacklistSerializer(serializer.Serializer):
    class Meta:
        model = Blacklists
        fields = '__all__'
