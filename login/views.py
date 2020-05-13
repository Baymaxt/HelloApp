from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response

from login.UserSerializers import UsersRegisterSerializer, UsersLoginSerializers
from login.models import Users
from login.util import token_confirm
from login.verifycode import vc


class UserRegisterView(CreateAPIView, ListAPIView):
    """
    post:
    进行注册
    get:
    获取验证码
    """
    queryset = Users.objects.all()
    serializer_class = UsersRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'code': 200,
                'msg': '注册成功',
                'data': {'uid': user.uid}
            })
        return Response({
            'code': 422,
            'msg': '注册失败',
            'data': {'info': serializer.errors}
        })

    def get(self, request, *args, **kwargs):
        verifyimg = vc.generate()
        code = vc.code
        return HttpResponse([verifyimg, code])


class UserLoginView(CreateAPIView):
    """
    post:登录
    """
    queryset = Users.objects.all()
    serializer_class = UsersLoginSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            uid = serializer.data.get('uid')
            token = token_confirm.generate_validate_token(uid)
            return Response({
                'code': 200,
                'msg': '登录成功',
                'data': {
                    'user': uid,
                    'token': token
                }
            })
        # 验证没通过
        else:
            return Response({
                'code': '1004',
                'msg': '登录失败，请重新登录',
                'data': {
                    'error': serializer.errors,
                    'token': ''
                }
            })

