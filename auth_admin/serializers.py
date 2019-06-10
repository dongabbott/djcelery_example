from rest_framework import serializers
from django.contrib.auth.models import User


class UserJWTSerializer(serializers.ModelSerializer):
    """获取token接口返回用户数据模型"""
    class Meta:
        model = User
        exclude = ('password',)