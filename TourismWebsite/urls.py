"""TourismWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# 新引入的模块
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 主页面路由
    path('index/', include('index.urls')),
    # 用户登录注册路由
    path('userprofile/', include('userprofile.urls')),
    # 用户重置密码路由
    path('password-reset/', include('password_reset.urls')),
    # 论坛路由
    path('article/', include('article.urls')),
    # 商城路由
    path('equipMall/', include('equipMall.urls')),
    # 酒店推荐路由
    path("hotel/", include('hotel.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # 添加这行
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
