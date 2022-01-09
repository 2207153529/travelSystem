from django.db import models
# 导入内建的User模型。
# from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
# from django.utils import timezone
# Django-taggit
# from taggit.managers import TaggableManager


class Hotel(models.Model):
    # 酒店标题图
    avatar = models.TextField()
    # 酒店名称
    name = models.TextField()
    # 酒店评分
    score = models.TextField()
    # 酒店信息。
    msg = models.TextField()
    # 酒店标签
    # tags = TaggableManager(blank=True)
    # 酒店价格
    price = models.FloatField()
    # 新增酒店地址
    addr = models.TextField()
    # detail网址
    href = models.TextField()
