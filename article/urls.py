# -*- coding: utf-8 -*-
# @Author: onezero
# @Date:   2020-03-11
# @Last Modified by:   100yang
# @Last Modified time: 2020-04-25
from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('ArticleList/', views.ArticleList, name='ArticleList'),
    path('ArticleDetail/<int:id>/', views.ArticleDetail, name='ArticleDetail'),
    path('ArticleCreate/', views.ArticleCreate, name='ArticleCreate'),
    path('ArticleDelete/<int:id>/', views.ArticleDelete, name='ArticleDelete'),
    path('ArticleUpdate/<int:id>/', views.ArticleUpdate, name='ArticleUpdate'),
    # path()
]
