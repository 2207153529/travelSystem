from django.db import models
# 导入内建的User模型。
# from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
# from django.utils import timezone
# Create your models here.


class navigator(models.Model):
    title = models.CharField(max_length=100)
    '''
    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)
    '''
    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    # 用户管理界面显示的数据名即为str()方法时的返回值内容

    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
