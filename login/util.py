from itsdangerous import URLSafeTimedSerializer as utsr
import base64
from django.conf import settings as django_settings

class Token:
    def __init__(self, security_key):
        self.security_key = security_key
        self.salt = base64.encodebytes(security_key.encode('utf8'))

    # 生成token
    def generate_validate_token(self, uid):
        serializer = utsr(self.security_key)
        return serializer.dumps(uid, self.salt)

    # 验证token
    def confirm_validate_token(self, token, expiration=36000):
        serializer = utsr(self.security_key)
        return serializer.loads(token, salt=self.salt, max_age=expiration)

    # 移除token
    def remove_validate_token(self, token):
        serializer = utsr(self.security_key)
        print(serializer.loads(token, salt=self.salt))
        return serializer.loads(token, salt=self.salt)


token_confirm = Token(django_settings.SECRET_KEY)
