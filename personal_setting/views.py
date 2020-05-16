from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from personal.views import PersonalViews


class PersonalSettingViews(PersonalViews):

    def post(self, request, *args, **kwargs):
        print(request.data.get('token'))
        user = self.confirm(request)
        if request.data.get('username') is not None:
            user.username = request.data.get('username')
        if request.data.get('gender') is not None:
            user.gender = request.data.get('gender')
        if request.data.get('age') is not None:
            user.age = request.data.get('age')
            print(request.data.get('age'))
        if request.data.get('email') is not None:
            user.email = request.data.get('email')
        if request.data.get('location') is not None:
            user.location = request.data.get('location')
        if request.data.get('portrait') is not None:
            user.portrait = self.get_portrait(request)
        user.save()
        return Response({
            'code': 200,
            'msg': '个人信息修改成功',
            'data': {}
        })

    def get_portrait(self, request):
        return None
