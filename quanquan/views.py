import datetime

from django.db.models import Q
# Create your views here.
from rest_framework.response import Response

from login.models import Posts, Votes, Subscriptions, Users
from personal.views import PersonalViews
from personal_setting.qiniu_manager import qm


class PostsViews(PersonalViews):
    """
    发布动态的类，包括发布文字图片、声音、投票等
    """
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
        if posts.post_category == 4:
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
        topic = request.data.get('topic')
        # 少于两项则返回错误信息，没法投票
        if request.data.get('option1') is not None:
            option1 = request.data.get('option1')
        else:
            return Response({
                'code': 422,
                'msg': '选项过少'
            })
        if request.data.get('option2') is not None:
            option2 = request.data.get('option2')
        else:
            return Response({
                'code': 422,
                'msg': '选项过少'
            })
        # 第3到6项可以没有，如果没有就置空
        if request.data.get('option3') is not None:
            option3 = request.data.get('option3')
        else:
            option3 = None
        if request.data.get('option4') is not None:
            option4 = request.data.get('option4')
        else:
            option4 = None
        if request.data.get('option5') is not None:
            option5 = request.data.get('option5')
        else:
            option5 = None
        if request.data.get('option6') is not None:
            option6 = request.data.get('option6')
        else:
            option6 = None
        Votes.objects.create(pid=posts, topic=topic, option1=option1, option2=option2, option3=option3, option4=option4,
                             option5=option5, option6=option6)


class QuanQuanViews(PersonalViews):
    """
    圈圈拉取好友动态，将按照时间把好友的动态显示出来，效果参考qq空间
    """
    def get(self, request, *args, **kwargs):
        user = self.confirm(request)
        if user.uid is None:
            return user
        # 查出所有关注用户的uid
        subs = Subscriptions.objects.filter(uid=user).only('following_uid')
        print(subs)
        sub_uid = []
        for i in range(0, len(subs)):
            sub_uid.append(subs[i].following_uid)
        print(sub_uid)
        # 所有关注的用户对象
        following = Users.objects.filter(uid__in=sub_uid)
        print(following)
        posts = Posts.objects.filter(Q(uid__in=following) | Q(uid=user.uid)).order_by('post_time')
        print(posts)
        return Response({
            'code': 200,
            'msg': '请求动态数据成功',
            'data': self.get_data(posts)
        })

    def get_data(self, posts):
        data = {}
        i = 0
        while i < len(posts):
            print(posts[i].uid)
            following = Users.objects.get(uid=posts[i].uid.uid)
            # 若是投票，则把投票内容写到data里
            if posts[i].post_category == 4:
                vote = Votes.objects.get(pid=posts[i])
                data.update({
                    'post' + str(i): {
                        'uid': following.uid,
                        'username': following.username,
                        'gender': following.gender,
                        'portrait': following.portrait,
                        'post_category': posts[i].post_category,
                        'post_time': posts[i].post_time,
                        'comment_amount': posts[i].comment_amount,
                        'forward_amount': posts[i].forward_amount,
                        'origin': posts[i].origin,
                        'vote': self.get_vote(vote)
                    }
                })
            # 若不是投票，则把文件七牛云链接写到data里
            else:
                data.update({
                    'post' + str(i): {
                        'uid': following.uid,
                        'username': following.username,
                        'gender': following.gender,
                        'portrait': following.portrait,
                        'post_category': posts[i].post_category,
                        'post_time': posts[i].post_time,
                        'comment_amount': posts[i].comment_amount,
                        'forward_amount': posts[i].forward_amount,
                        'origin': posts[i].origin,
                        'post_content': posts[i].post_content,
                    }
                })
            i = i + 1
        return data

    def get_vote(self, vote):
        data = {}
        data.update({
            'topic': vote.topic,
            'option1': vote.option1,
            'option1_amount': vote.option1_amount,
            'option2': vote.option2,
            'option2_amount': vote.option2_amount,
        })
        # 投票前两项一定存在，3到6项若存在则写入data
        if vote.option3 is not None:
            data.update({
                'option3': vote.option3,
                'option3_amount': vote.option3_amount,
            })
        if vote.option4 is not None:
            data.update({
                'option4': vote.option4,
                'option4_amount': vote.option4_amount,
            })
        if vote.option5 is not None:
            data.update({
                'option5': vote.option5,
                'option5_amount': vote.option5_amount,
            })
        if vote.option6 is not None:
            data.update({
                'option6': vote.option6,
                'option6_amount': vote.option6_amount,
            })
        return data
