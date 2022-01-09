# 引入views.py
from . import views
from django.urls import path
from django.contrib import admin


app_name = 'index'
urlpatterns = [
    # path函数将url映射到视图
    # 首页路由
    path('index_list', views.index_list, name='index_list'),
    # 管理员首页路由
    path('admin/', admin.site.urls),
]
