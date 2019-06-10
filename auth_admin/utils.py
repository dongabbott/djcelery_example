from .serializers import UserJWTSerializer
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
import re


def jwt_response_payload_handler(token, user=None, request=None):
    """为返回的结果添加用户相关信息"""

    return {
        'token': token,
        'user': UserJWTSerializer(user, context={'request': request}).data
    }


def get_user_by_email(email):
    """
    添加通过邮箱查询用户的方法
    """
    try:
        if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', email):
            user = User.objects.get(email=email)
        else:
            user = User.objects.get(username=email)
    except User.DoesNotExist:
        return None
    else:
        return user


class UserByUsernameEmail(ModelBackend):
    """添加支持邮箱登录"""

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_user_by_email(username)  # username 可能是用户名也可能是邮箱
        return user