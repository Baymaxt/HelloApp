# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# 身份认证表，主播认证大神认证等
class Authentications(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    # 认证名称
    authentication_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authentications'


# 黑名单表
class Blacklists(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    # 被拉黑的uid
    black_uid = models.CharField(max_length=20)
    # 是否互相拉黑
    mutual_black = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blacklists'


# 所有涉及金币的交易的订单表
class CoinOrders(models.Model):
    # 订单号
    oid = models.AutoField(primary_key=True)
    # 收款方uid
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    # 付款方uid
    from_uid = models.CharField(max_length=20)
    # 金币数量
    coin_figure = models.IntegerField()
    order_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coin_orders'


# 收藏表
class Collections(models.Model):
    pid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='pid')
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    collect_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collections'


# 评论表
class Comments(models.Model):
    cid = models.IntegerField(primary_key=True)
    pid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='pid')
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    comment_time = models.DateTimeField(blank=True, null=True)
    comment_content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


# 优惠券表
class Coupons(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    # 满reach减subtract，reach为优惠门槛
    reach = models.IntegerField()
    # 满减金额
    subtract = models.IntegerField()
    # 有效期
    indate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupons'


# 动态表
class Posts(models.Model):
    pid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    # 动态种类
    # 1为文字图片，内容在PostContent表中
    # 2为游戏截图，内容在PostContent表中
    # 3为声音，内容在SoundsContent表中
    # 4为投票，内容在Votes表中
    post_category = models.IntegerField()
    # 评论数
    comment_amount = models.IntegerField(blank=True, null=True)
    # 发表时间
    post_time = models.DateTimeField(blank=True, null=True)
    # 转发数
    forward_amount = models.IntegerField(blank=True, null=True)
    # 若为转发的动态，则填入原动态uid
    origin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class PostsContent(models.Model):
    pid = models.ForeignKey(Posts, models.DO_NOTHING, db_column='pid')
    # 文字图片内容
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts_content'


# 礼物表
class Presents(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    # 送礼的人的uid
    from_uid = models.CharField(max_length=20)
    # 礼物种类，飞机跑车啥的
    present_category = models.CharField(max_length=20, blank=True, null=True)
    receive_time = models.DateTimeField(blank=True, null=True)
    # 是否被兑换成金币
    is_exchange = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presents'


class PresentsCategories(models.Model):
    # 礼物种类的名称
    present_category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presents_categories'


class SoundsContent(models.Model):
    pid = models.ForeignKey(Posts, models.DO_NOTHING, db_column='pid')
    # 声音文件的路径
    sound = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sounds_content'


# 关注表
class Subscriptions(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    # 关注谁就填谁的uid
    following_uid = models.CharField(max_length=20)
    # 俩人是否是互相关注
    mutual_following = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


# 个人标签表
class Tags(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    tag_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


# 所有与人民币有关的交易
class TransactionDetails(models.Model):
    # 订单号
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    # 是否是提现，1为提现，0为充值
    is_withdraw = models.IntegerField()
    # 提现或充值的金额
    transaction_figure = models.IntegerField()
    transaction_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_details'


class Users(models.Model):
    uid = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=20, null=False)
    username = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField()
    # 头像路径
    portrait = models.CharField(max_length=255, blank=True, null=True)
    # 若进行了实名认证则填入真实姓名
    real_name = models.CharField(max_length=50, blank=True, null=True)
    # 若进行了实名认证则填入身份证号
    id_number = models.CharField(db_column='ID_number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    # 关注数
    following_amount = models.IntegerField(blank=True, null=True)
    # 粉丝数
    follower_amount = models.IntegerField(blank=True, null=True)
    # 互相关注数，即好友数
    mutual_follow_amount = models.IntegerField(blank=True, null=True)
    # 所在地
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


# 投票表
class Votes(models.Model):
    pid = models.ForeignKey(Posts, models.DO_NOTHING, db_column='pid')
    # 投票主题
    topic = models.CharField(max_length=255, blank=True, null=True)
    # 选项1
    option1 = models.CharField(max_length=100, blank=True, null=True)
    # 选项1的得票数，后边以此类对，最多6个选项
    option1_amount = models.IntegerField(blank=True, null=True)
    option2 = models.CharField(max_length=100, blank=True, null=True)
    option2_amount = models.IntegerField(blank=True, null=True)
    option3 = models.CharField(max_length=100, blank=True, null=True)
    option3_amount = models.IntegerField(blank=True, null=True)
    option4 = models.CharField(max_length=100, blank=True, null=True)
    option4_amount = models.IntegerField(blank=True, null=True)
    option5 = models.CharField(max_length=100, blank=True, null=True)
    option5_amount = models.IntegerField(blank=True, null=True)
    option6 = models.CharField(max_length=100, blank=True, null=True)
    option6_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'votes'


# 钱包表
class Wallets(models.Model):
    wid = models.IntegerField(primary_key=True)
    uid = models.ForeignKey(Users, models.DO_NOTHING, db_column='uid')
    # 人民币余额
    balance = models.IntegerField(blank=True, null=True)
    # 金币余额
    coin_amount = models.IntegerField(blank=True, null=True)
    # 可提现金币数
    can_withdraw = models.IntegerField(blank=True, null=True)
    # 优惠券数
    coupon_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallets'
