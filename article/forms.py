# -*- coding: utf-8 -*-
# @Author: onezero
# @Date:   2020-03-11
# @Last Modified by:   onezero
# @Last Modified time: 2020-03-11
from django import forms

# 引入文章模型
from .models import ArticlePost


class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 模型的来源
        model = ArticlePost
        # 定义表单中包含的数据
        fields = ('title', 'body')
