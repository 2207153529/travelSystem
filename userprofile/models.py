from django.db import models

# Create your models here.


class userprofile(models.Model):
    # 用户名
    username = models.CharField(max_length=100)
    # 用户邮箱
    email = models.CharField(max_length=100)
    # 用户密码
    password = models.CharField(max_length=100)
