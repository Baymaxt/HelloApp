login模块下有一个util.py文件，是封装的一个token生成及验证文件，可以直接拿来用，不会用可以翻老师的视频听一听。
里面是一个单例类，用的时候直接from login.util import token_confirm，不要直接导入Token

应用personal_interaction和personal_tools已经建好
personal_interaction负责圈圈互动中的我的评论，我的动态，我的收藏
personal_tools负责‘我的’里面的‘必备工具’中的我的订单、优惠中心、我的礼物、我的钱包等

已经写好的代码如果要做修改一定告诉我一声

models文件在login里，自己导一下

python3.7

django2.2

mysql5.7.18