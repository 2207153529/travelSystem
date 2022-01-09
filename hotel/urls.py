from . import views
from django.urls import path
app_name = 'hotel'

urlpatterns = [
    # 目前还没有urls
]

urlpatterns = [
    # path函数将url映射到视图
    path('hotel-list/', views.hotel_list, name='hotel_list'),
    # 酒店详情
    path('hotel-detail/<int:id>/', views.hotel_detail, name='hotel_detail'),
]
