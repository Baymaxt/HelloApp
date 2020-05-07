from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from login.UserSerializers import UserRegisterSerializer
from login.models import Users


class UserRegisterView(GenericAPIView):
    """
    post: 进行注册
    """
    queryset = Users.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'code': 200,
                'msg': '注册成功',
                'user_id': user.id
            })
        return Response({
            'code': 105,
            'msg': '注册失败',
            'info': serializer.errors
        })

