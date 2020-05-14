
# Create your views here.
from rest_framework import serializers
from rest_framework.response import Response

from login.models import Users
from personal.views import PersonalViews
from personal_sub_black.PersonSubBlackSerializers import *


class MyFollowingViews(PersonalViews):
    queryset = Subscriptions.objects.all()
    serializer_class = MyFollowSerializer

    def get(self, request, *args, **kwargs):
        user = self.confirm(request)
        if not user.uid:
            return user
        if request.query_params.get('operation') == 'follow':
            following_user = Users.objects.filter(uid=request.query_params.get('uid'))
            response = self.follow(user, following_user)
            return response
        elif request.query_params.get('operation') == 'unfollow':
            following_user = Users.objects.filter(uid=request.query_params.get('uid'))
            response = self.unfollow(user, following_user)
            return response

        else:
            following = self.queryset.filter(uid=user.uid).values('following_uid')
            users = Users.objects.filter(uid__in=following)
            data = self.get_data(users)
            return Response({
                'code': '200',
                'msg': '我的关注',
                'data': data
            })

    def follow(self, user, following_user):
        try:
            following = Subscriptions.objects.get(uid=following_user[0], following_uid=user.uid)
            print(following)
            following.mutual_following = 1
            following.save()
            print(following.mutual_following)
            subs = Subscriptions(uid=user, following_uid=following_user[0].uid, mutual_following=1)
        except:
            subs = Subscriptions(uid=user, following_uid=following_user[0].uid, mutual_following=0)
        subs.save()
        return Response({
            'code': '200',
            'msg': '关注成功',
            'data': {}
        })

    def unfollow(self, user, following_user):
        try:
            following = Subscriptions.objects.get(uid=following_user[0], following_uid=user.uid)
            following.mutual_following = 0
            following.save()
            subs = Subscriptions.objects.filter(uid=user, following_uid=following_user[0].uid)
            subs.delete()
        except:
            subs = Subscriptions.objects.filter(uid=user, following_uid=following_user[0].uid)
            subs.delete()
        return Response({
            'code': '200',
            'msg': '取关成功',
            'data': {}
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
