from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from login.models import Users
from personal.views import PersonalViews
from personal_sub_black.PersonSubBlackSerializers import *


class MyFollowingViews(PersonalViews):
    queryset = Subscriptions.objects.all()
    serializer_class = MyFollowSerializer

    def get(self, request, *args, **kwargs):
        user = self.confirm(request)
        following = self.queryset.filter(uid=user.uid).values('following_uid')
        users = Users.objects.filter(uid__in=following)
        data = self.get_data(users)
        return Response({
            'code': '200',
            'msg': '我的关注',
            'data': data
        })


class MyFollowerViews(PersonalViews):
    queryset = Subscriptions.objects.all()
    serializer_class = MyFollowSerializer

    def get(self, request, *args, **kwargs):
        user = self.confirm(request)
        follower = self.queryset.filter(following_uid=user.uid).values('uid')
        users = Users.objects.filter(uid__in=follower)
        data = self.get_data(users)
        return Response({
            'code': '200',
            'msg': '我的粉丝',
            'data': data
        })


class MyMutualFollowViews(PersonalViews):
    queryset = Subscriptions.objects.all()
    serializer_class = MyFollowSerializer

    def get(self, request, *args, **kwargs):
        user = self.confirm(request)
        follower = self.queryset.filter(uid=user.uid, mutual_following=1).values('uid')
        users = Users.objects.filter(uid__in=follower)
        data = self.get_data(users)
        return Response({
            'code': '200',
            'msg': '互相关注',
            'data': data
        })


class MyBlacklistViews(PersonalViews):
    queryset = Blacklists.objects.all()
    serializer_class = MyBlacklistSerializer

    def get(self, request, *args, **kwargs):
        user = self.confirm(request)
        blacklist = self.queryset.filter(uid=user.uid).values('black_uid')
        users = Users.objects.filter(uid__in=blacklist)
        data = self.get_data(users)
        return Response({
            'code': '200',
            'msg': '我的黑名单',
            'data': data
        })
