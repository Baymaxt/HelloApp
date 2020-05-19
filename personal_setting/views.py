from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from personal.views import PersonalViews
from personal_setting.qiniu_manager import qm


class PersonalSettingViews(PersonalViews):

    def post(self, request, *args, **kwargs):
        user = self.confirm(request)
        if user.uid is None:
            return user
        if request.data.get('username') is not None:
            user.username = request.data.get('username')
        if request.data.get('gender') is not None:
            user.gender = request.data.get('gender')
        if request.data.get('age') is not None:
            user.age = request.data.get('age')
        if request.data.get('email') is not None:
            user.email = request.data.get('email')
        if request.data.get('location') is not None:
            user.location = request.data.get('location')
        if request.data.get('portrait') is not None:
            user.portrait = self.get_portrait(request, user.uid)
        user.save()
        return Response({
            'code': 200,
            'msg': '个人信息修改成功',
            'data': {'token': request.data.get('token')}
        })

    def get_portrait(self, request, uid):
        portrait = request.FILES.get('portrait').read()
        picname = 'portrait' + uid
        return qm.upload(picname, portrait)
