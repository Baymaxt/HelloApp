from django.shortcuts import render


# Create your views here.
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from login.models import Users
from personal_center.PersonalSerializers import PersonalSerializer
from login.util import token_confirm


class PersonalViews(ListAPIView):
    """
    get:
    返回‘我的’界面中的用户名，头像，粉丝数，关注数，互相关注数等<br>
    需求参数：
    token
    """
    queryset = Users.objects.all()
    serializer_class = PersonalSerializer

    def get(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        # 获取token
        token = request.query_params.get('token')
        print(token)
        # 检查token
        try:
            uid = token_confirm.confirm_validate_token(token)
            print(uid)
        except APIException as e:
            print(e)
            return Response({
                'code': 1006,
                'msg': 'token失效',
                'data': {}
            })
        # 检查用户是否存在
        try:
            user = Users.objects.get(uid=uid)
            print(user)
        except APIException as e:
            print(e)
            return Response({
                'code': 1006,
                'msg': '用户不存在',
                'data': {}
            })
        # 返回数据
        return Response({
            'code': 200,
            'msg': '',
            'data': {
                'username': user.username,
                'portrait': user.portrait,
                'following': user.following_amount,
                'follower': user.follower_amount,
                'mutual': user.mutual_follow_amount
            }
        })


