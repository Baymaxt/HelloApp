from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response

from login.UserSerializers import UsersRegisterSerializer
from login.models import Users


class UserRegisterView(CreateAPIView, ListAPIView):
    """
    post: 进行注册
    get: 获取验证码
    """
    queryset = Users.objects.all()
    serializer_class = UsersRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request, 11111111)
        print(request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'code': 200,
                'msg': '注册成功',
                'user_id': user.uid
            })
        return Response({
            'code': 105,
            'msg': '注册失败',
            'info': serializer.errors
        })

    def get(self, request, *args, **kwargs):
        return Response({
            'code': 200,
        })

