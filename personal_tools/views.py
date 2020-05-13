import json

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from personal_tools.PersonToolsSerializers import *
from personal.views import PersonalViews
"""
‘我的’里面的‘必备工具’中的我的订单、优惠中心、我的礼物、我的钱包等逻辑写在这里
"""


class MyWalletView(PersonalViews):
    queryset = Wallets.objects.all()
    serializer_class = MyWalletSerializer

    def get(self, request, *args, **kwargs):
        # 获取token
        token = request.query_params.get('token')
        # 检查token
        user = self.confirm(token)
        wallet = Wallets.objects.get(uid=user.uid)
        return Response({
            'code': 200,
            'msg': '',
            'data': {
                'balance': wallet.balance,
                'coin_amount': wallet.coin_amount,
                'can_withdraw': wallet.can_withdraw,
                'coupons_amount': wallet.coupons_amount
            }
        })


class MyOrderView(PersonalViews):
    queryset = CoinOrders.objects.all()
    serializer_class = MyOrderSerializer

    def get(self, request, *args, **kwargs):
        # 获取token
        token = request.query_params.get('token')
        # 检查token
        user = self.confirm(token)
        orders = CoinOrders.objects.filter(uid=user.uid)
        data = self.get_data(orders)
        return Response({
            'code': 200,
            'msg': '',
            'data': data
        })

    def get_data(self, orders):
        data = {}
        i = 0
        while i < len(orders):
            data.update({
                'order' + str(i): {
                    'oid': orders[i].oid,
                    'uid': orders[i].uid.uid,
                    'from_uid': orders[i].from_uid,
                    'coin_figure': orders[i].from_uid,
                    'order_time': str(orders[i].order_time)
                }
            })
            i = i + 1
        return data


class MyPresentView(PersonalViews):
    queryset = Presents.objects.all()
    serializer_class = MyPresentSerializer

    def get(self, request, *args, **kwargs):
        # 获取token
        token = request.query_params.get('token')
        # 检查token
        user = self.confirm(token)
        presents = Presents.objects.filter(uid=user.uid)
        data = self.get_data(presents)
        return Response({
            'code': 200,
            'msg': '',
            'data': data
        })

    def get_data(self, presents):
        data = {}
        i = 0
        while i < len(presents):
            data.update({
                'order' + str(i): {
                    'uid': presents[i].uid.uid,
                    'from_uid': presents[i].from_uid,
                    'receive_time': str(presents[i].receive_time),
                    'is_exchange': presents[i].is_exchange
                }
            })
            i = i + 1
        return data


class MyCouponView(PersonalViews):
    queryset = Coupons.objects.all()
    serializer_class = MyCouponSerializer

    def get(self, request, *args, **kwargs):
        # 获取token
        token = request.query_params.get('token')
        # 检查token
        user = self.confirm(token)
        coupons = Coupons.objects.filter(uid=user.uid)
        data = self.get_data(coupons)
        return Response({
            'code': 200,
            'msg': '',
            'data': data
        })

    def get_data(self, coupons):
        data = {}
        i = 0
        while i < len(coupons):
            data.update({
                'order' + str(i): {
                    'uid': coupons[i].uid.uid,
                    'reach': coupons[i].reach,
                    'subtract': coupons[i].subtract,
                    'indate': str(coupons[i].indate)
                }
            })
            i = i + 1
        return data
