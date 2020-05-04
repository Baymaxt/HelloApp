# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Authentications(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    authentication_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'authentications'


class Blacklists(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    black_uid = models.CharField(max_length=20)
    mutual_black = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'blacklists'


class CoinOrders(models.Model):
    oid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    from_uid = models.CharField(max_length=20)
    coin_figure = models.IntegerField()
    order_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coin_orders'


class Collections(models.Model):
    pid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='pid')
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    collect_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collections'


class Comments(models.Model):
    cid = models.IntegerField(primary_key=True)
    pid = models.ForeignKey('Posts', models.DO_NOTHING, db_column='pid')
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    comment_time = models.DateTimeField(blank=True, null=True)
    comment_content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comments'


class Coupons(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    reach = models.IntegerField()
    subtract = models.IntegerField()
    indate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupons'


class Posts(models.Model):
    pid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    post_category = models.IntegerField()
    comment_amount = models.IntegerField(blank=True, null=True)
    post_time = models.DateTimeField(blank=True, null=True)
    forward_amount = models.IntegerField(blank=True, null=True)
    origin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class PostsContent(models.Model):
    pid = models.ForeignKey(Posts, models.DO_NOTHING, db_column='pid')
    content = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts_content'


class Presents(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    from_uid = models.CharField(max_length=20)
    present_category = models.CharField(max_length=20, blank=True, null=True)
    receive_time = models.DateTimeField(blank=True, null=True)
    is_exchange = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presents'


class PresentsCategories(models.Model):
    present_category = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presents_categories'


class SoundsContent(models.Model):
    pid = models.ForeignKey(Posts, models.DO_NOTHING, db_column='pid')
    sound = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sounds_content'


class Subscriptions(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    following_uid = models.CharField(max_length=20)
    mutual_following = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'


class Tags(models.Model):
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid', blank=True, null=True)
    tag_name = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tags'


class TransactionDetails(models.Model):
    tid = models.AutoField(primary_key=True)
    uid = models.ForeignKey('Users', models.DO_NOTHING, db_column='uid')
    is_withdraw = models.IntegerField()
    transaction_figure = models.IntegerField()
    transaction_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction_details'


class Users(models.Model):
    uid = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField()
    portrait = models.CharField(max_length=255, blank=True, null=True)
    real_name = models.CharField(max_length=50, blank=True, null=True)
    id_number = models.CharField(db_column='ID_number', max_length=50, blank=True, null=True)  # Field name made lowercase.
    following_amount = models.IntegerField(blank=True, null=True)
    follower_amount = models.IntegerField(blank=True, null=True)
    mutual_follow_amount = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Votes(models.Model):
    pid = models.ForeignKey(Posts, models.DO_NOTHING, db_column='pid')
    topic = models.CharField(max_length=255, blank=True, null=True)
    option1 = models.CharField(max_length=100, blank=True, null=True)
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


class Wallets(models.Model):
    wid = models.IntegerField(primary_key=True)
    uid = models.ForeignKey(Users, models.DO_NOTHING, db_column='uid')
    balance = models.IntegerField(blank=True, null=True)
    coin_amount = models.IntegerField(blank=True, null=True)
    can_withdraw = models.IntegerField(blank=True, null=True)
    coupon_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wallets'
