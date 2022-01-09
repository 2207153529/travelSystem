from django.db import models

# Create your models here.

# from django.contrib.auth.models import User

# deal time
from django.utils import timezone

# 博客文章数据模型


# class Category(models.Model):
#     """
#     Django 要求模型必须继承 models.Model 类。
#     Category 只需要一个简单的分类名 name 就可以了。
#     CharField 指定了分类名 name 的数据类型，CharField 是字符型，
#     CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
#     然后给name设置了一个'分类'的名称
#     """
#     name = models.CharField('分类', max_length=100)


# class Tags(models.Model):
#     """
#     标签 Tag 也比较简单，和 Category 一样。
#     再次强调一定要继承 models.Model 类！
#     """
#     name = models.CharField('标签', max_length=100)


class ArticlePost(models.Model):
    author = models.CharField(max_length=10000)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=100)
    body = models.TextField()
    createdtime = models.DateTimeField(default=timezone.now)
    updatetime = models.DateTimeField(auto_now=True)
    # category = models.ForeignKey(
    #     Category, on_delete=models.CASCADE, verbose_name='分类', default='1')
    # tags = models.ManyToManyField(Tags, blank=True)
    # 定义元数据

    class Meta:
        #   ordering 指定模型返回的数据的排列顺序
        #   '-createdtime' 表明数据以倒序排列

        ordering = ('-createdtime',)
    # __str__ 定义当调用对象的 str()　方法时返回值的内容

    def __str__(self):
        return self.title
