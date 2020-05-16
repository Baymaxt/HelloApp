
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
            # 若uid不存在，此时confirm返回的是errorresponse
            return user
        if request.query_params.get('operation') == 'follow':
            following_user = Users.objects.get(uid=request.query_params.get('uid'))
            response = self.follow(user, following_user)
            return response
        elif request.query_params.get('operation') == 'unfollow':
            following_user = Users.objects.get(uid=request.query_params.get('uid'))
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
            # 若已经存在记录，则把following_user和user的mutual_follow置1
            following = Subscriptions.objects.get(uid=following_user, following_uid=user.uid)
            following.mutual_following = 1
            following.save()
            # 对user与following_user的关注数、粉丝数、互关数做出相应改变
            following_user.follower_amount += 1
            following_user.mutual_follow_amount += 1
            following_user.save()
            subs = Subscriptions(uid=user, following_uid=following_user.uid, mutual_following=1)
        except:
            following_user.follower_amount += 1
            following_user.save()
            subs = Subscriptions(uid=user, following_uid=following_user.uid, mutual_following=0)
        subs.save()
        return Response({
            'code': '200',
            'msg': '关注成功',
            'data': {}
        })

    def unfollow(self, user, following_user):
        try:
            following = Subscriptions.objects.get(uid=following_user, following_uid=user.uid)
            following.mutual_following = 0
            following.save()
            # 对user与following_user的关注数、粉丝数、互关数做出相应改变
            following_user.follower_amount -= 1
            following_user.mutual_follow_amount -= 1
            following_user.save()
            subs = Subscriptions.objects.filter(uid=user, following_uid=following_user.uid)
        except:
            following_user.follower_amount -= 1
            following_user.save()
            subs = Subscriptions.objects.filter(uid=user, following_uid=following_user.uid)
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
        if not user.uid:
            # 若uid不存在，此时confirm返回的是errorresponse
            return user
        if request.query_params.get('operation') == 'block':
            block_user = Users.objects.get(uid=request.query_params.get('uid'))
            response = self.block(user, block_user)
            return response
        elif request.query_params.get('operation') == 'unblock':
            unblock_user = Users.objects.get(uid=request.query_params.get('uid'))
            response = self.unblock(user, unblock_user)
            return response
        else:
            blacklist = self.queryset.filter(uid=user.uid).values('black_uid')
            users = Users.objects.filter(uid__in=blacklist)
            data = self.get_data(users)
            return Response({
                'code': '200',
                'msg': '黑名单',
                'data': data
            })

    def block(self, user, block_user):
        try:
            # 若已被对方拉黑，则把mutual_black置1
            blacklist = Blacklists.objects.get(uid=block_user, black_uid=user.uid)
            blacklist.mutual_black = 1
            blacklist.save()
            # 新建blacklist对象
            black = Blacklists(uid=user, black_uid=block_user.uid, mutual_black=1)
        except:
            black = Blacklists(uid=user, black_uid=block_user.uid, mutual_black=0)
        black.save()
        return Response({
            'code': '200',
            'msg': '拉黑成功',
            'data': {}
        })

    def unblock(self, user, unblock_user):
        try:
            # 若已被对方拉黑，则把mutual_black置1
            blacklist = Blacklists.objects.get(uid=unblock_user, black_uid=user.uid)
            blacklist.mutual_black = 0
            blacklist.save()
            # 新建blacklist对象
            black = Blacklists.objects.get(uid=user, black_uid=unblock_user.uid)
        except:
            black = Blacklists.objects.get(uid=user, black_uid=unblock_user.uid)
        black.delete()
        return Response({
            'code': '200',
            'msg': '取消拉黑成功',
            'data': {}
        })

