from django.shortcuts import render, redirect
# Create your views here.
from django.db.models import Q
# 导入数据模型ArticlePost
from .models import Hotel
# 引入分页模块
from django.core.paginator import Paginator
from static.spider import quanerCrawl


def getWebHotel():
    # address = ['beijing_city']
    address = ['beijing_city', 'shanghai_city', 'guangzhou', 'chengdu']
    for addr in address:
        hotel_item = quanerCrawl.getCity(addr).getDetail()
        i = 0
        while i < len(hotel_item[0]):
            # print(hotel_item[2][i])
            if Hotel.objects.filter(name=hotel_item[1][i]):
                continue
            new_hotel = Hotel(
                avatar=hotel_item[0][i],
                name=hotel_item[1][i],
                score=hotel_item[2][i],
                msg=hotel_item[4][i],
                # tags=addr,
                price=hotel_item[3][i],
                addr=addr,
                href=hotel_item[5][i]
            )
            new_hotel.save()
            i = i + 1


def hotel_list(request):
    # getWebHotel()
    hotel_list = Hotel.objects.all()
    addr = request.GET.get('addr')
    search = request.GET.get('search')
    # 用户搜索逻辑
    if search:
        # 用 Q对象 进行联合搜索
        hotel_list = Hotel.objects.filter(
            Q(name__icontains=search) | Q(msg__icontains=search)
        )
    else:
        # 将 search 参数重置为空
        search = ''
    if addr == 'shanghai_city':
        hotel_list = Hotel.objects.filter(Q(addr__icontains=addr))
    elif addr == 'guangzhou':
        hotel_list = Hotel.objects.filter(Q(addr__icontains=addr))
    elif addr == 'beijing_city':
        hotel_list = Hotel.objects.filter(Q(addr__icontains=addr))
    elif addr == 'chengdu':
        hotel_list = Hotel.objects.filter(Q(addr__icontains=addr))
    paginator = Paginator(hotel_list, 9)
    page = request.GET.get('page')
    hotels = paginator.get_page(page)
    # 增加 search 到 context
    print(hotel_list[0].avatar)
    context = {'hotels': hotels, 'search': search, 'addr': addr}
    return render(request, 'hotel/list.html', context)


def hotel_detail(request, id):
    # 取出对应的酒店
    hotel = Hotel.objects.get(id=id)
    # 重定向到hotel.href
    return redirect(hotel.href)
