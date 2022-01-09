from django.shortcuts import render
from .models import navigator
# Create your views here.
# 导入 HttpResponse 模块
# from django.http import HttpResponse

# 视图函数


def index_list(request):
    # 取出所有博客文章
    cells = navigator.objects.all()
    # 需要传递给模板（templates）的对象
    context = {'cells': cells}
    # render函数：载入模板，并返回context对象
    return render(request, 'index/list.html', context)
