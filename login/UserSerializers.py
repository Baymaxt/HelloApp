from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from login.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


# 注册的序列化器
class UsersRegisterSerializer(serializers.Serializer):
    uid = serializers.CharField(required=True, max_length=20)
    password = serializers.CharField(required=True, min_length=6, max_length=20,
                                     error_messages={
                                         'min_length': '最小长度6位',
                                         'max_length': '最大长度20位'
                                     })
    password2 = serializers.CharField(min_length=6, max_length=20,
                                     error_messages={
                                         'min_length': '最小长度6位',
                                         'max_length': '最大长度20位'
                                     })

    # 验证uid是否唯一
    def validate_uid(self, attrs):
        print(attrs)
        user = Users.objects.filter(uid=attrs).first()
        if user:
            raise serializers.ValidationError("用户名已经被占用")
        return attrs

    # 验证两次密码是否一致
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("两次密码不一致")
        return attrs

    # 存进数据库
    def create(self, validated_data):
        user = Users()
        password = validated_data.get('password')
        password = make_password(password)  # 对密码加密
        user.uid = validated_data.get('uid')
        user.password = password
        user.save()
        return user


# 登录的序列化器
class UsersLoginSerializers(serializers.Serializer):
    uid = serializers.CharField(required=True, max_length=20)
    password = serializers.CharField(required=True, min_length=6, max_length=20,
                                     error_messages={
                                         'min_length': '最小长度6位',
                                         'max_length': '最大长度20位'
                                     })

    def validate(self, attrs):
        uid = attrs.get('uid')
        password = attrs.get('password')
        user = Users.objects.filter(uid=uid)
        if not user.exists():
            raise serializers.ValidationError({'uid': '用户不存在'})
        user = user.first()
        if not check_password(password, user.password):
            raise serializers.ValidationError({'invalid': '用户名或密码错误'})
        return attrs
