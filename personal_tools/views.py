from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from personal_tools.PersonToolsSerializers import *
"""
‘我的’里面的‘必备工具’中的我的订单、优惠中心、我的礼物、我的钱包等逻辑写在这里
"""


class MyWalletView(ListAPIView):
    queryset = Wallets.objects.all()
    serializer_class = MyWalletSerializer


class MyOrderView(object):
    queryset = CoinOrders.objects.all()
    serializer_class = MyOrderSerializer


class MyPresentView(object):
    queryset = Presents.objects.all()
    serializer_class = MyPresentSerializer


class MyCouponView(object):
    queryset = Coupons.objects.all()
    serializer_class = MyCouponSerializer
