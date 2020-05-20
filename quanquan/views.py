import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from login.models import Posts, Votes
from personal.views import PersonalViews
from personal_setting.qiniu_manager import qm


class PostsView(PersonalViews):

    def post(self, request, *args, **kwargs):
        user = self.confirm(request)
        if user.uid is None:
            return user
        posts = Posts.objects.create(uid=user,
                                     post_category=int(request.data.get('post_category')),
                                     post_time=datetime.datetime.now())
        # 如果origin不为空则证明此动态是转发的，值为被转发的动态的pid
        if request.data.get('origin') is not None:
            posts.origin = request.data.get('origin')
        # 如果post_category == 4则证明这条动态是一个投票，新建一个投票对象。
        if posts.post_category == '4':
            self.get_vote(request, posts)
        else:
            posts.post_content = self.get_content(request, posts.pid)
        posts.save()
        return Response({
            'code': 200,
            'msg': '发布成功',
            'data': {}
        })

    # 上传文件，同时返回内容
    def get_content(self, request, pid):
        pname = 'post' + str(pid)
        return qm.upload(request, pname)

    # 建立对应的投票信息
    def get_vote(self, request, posts):
        vote = Votes.objects.create(pid=posts)
        vote.topic = request.data.get('topic')
        if request.data.get('option1') is not None:
            vote.option1 = request.data.get('option1')
        if request.data.get('option2') is not None:
            vote.option2 = request.data.get('option2')
        if request.data.get('option3') is not None:
            vote.option3 = request.data.get('option3')
        if request.data.get('option4') is not None:
            vote.option4 = request.data.get('option4')
        if request.data.get('option5') is not None:
            vote.option5 = request.data.get('option5')
        if request.data.get('option6') is not None:
            vote.option6 = request.data.get('option6')
        vote.save()
