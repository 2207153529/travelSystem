# 引入views.py
from . import views
from django.urls import path

app_name = 'equipMall'

urlpatterns = [
    # path函数将url映射到视图
    path('equip_list/', views.equip_list, name='equip_list'),
]
