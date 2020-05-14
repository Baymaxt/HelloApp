from rest_framework import serializers

from login.models import Wallets, CoinOrders, Presents, Coupons


class MyWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallets
        fields = '__all__'


class MyOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinOrders
        fields = '__all__'


class MyPresentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Presents
        fields = '__all__'


class MyCouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupons
        fields = '__all__'
