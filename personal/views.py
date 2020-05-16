from django.shortcuts import render

# Create your views here.
from itsdangerous import SignatureExpired
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from login.models import Users
from personal.PersonalSerializers import PersonalSerializer
from login.util import token_confirm


class PersonalViews(ListAPIView, CreateAPIView):
    """
    get:
    返回‘我的’界面中的用户名，头像，粉丝数，关注数，互相关注数等<br>
    需求参数：
    token
    """
    queryset = Users.objects.all()
    serializer_class = PersonalSerializer

    def get(self, request, *args, **kwargs):
        # 检查token，获取用户对象
        user = self.confirm(request)
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

    # 检验token，检查用户是否存在
    def confirm(self, request):
        """
        :param request: 将resquest传入
        :return: 返回对应的user对象
        """
        if request.query_params.get('token') is not None:
            token = request.query_params.get('token')
        else:
            token = request.data.get('token')
        try:
            uid = token_confirm.confirm_validate_token(token)
        except SignatureExpired as e:
            print(e)
            return Response({
                'code': 422,
                'msg': 'token失效',
                'data': {}
            })
        # 检查用户是否存在
        try:
            user = Users.objects.get(uid=uid)
        except APIException as e:
            print(e)
            return Response({
                'code': 422,
                'msg': '用户不存在',
                'data': {}
            })
        # 返回一个Users的对象
        return user

    def get_data(self, dataobj):
        """
        可重写此方法用来获取查询结果集中的数据，以下代码仅做示例
        data = {}
        i = 0
        while i < len(dataobj):
            data.update({
                'order' + str(i): {
                    'attr': dataobj[i].attr,
                    # uid是外键，外键的真实值是个user对象，所以要.uid两次
                    'uid': dataobj[i].uid.uid,
                    # 时间是datetime类型的数据，要加str()转换成字符串
                    'time': str(dataobj[i].time)
                }
            })
            i = i + 1
        return data
        :param dataobj: queryset对象
        :return: query中的数据构成的字典
        """
        data = {}
        i = 0
        while i < len(dataobj):
            data.update({
                'user' + str(i): {
                    'uid': dataobj[i].uid,
                    'username': dataobj[i].username,
                    'gender': dataobj[i].gender,
                    'portrait': dataobj[i].portrait,
                    'age': dataobj[i].age,
                }
            })
            i = i + 1
        return data
