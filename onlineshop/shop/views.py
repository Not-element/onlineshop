from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from buyer.models import BuyerInfo
from seller.models import Goods, SellerInfo


def index(request):
    posts = Goods.objects.order_by()  # 默认按时间排序

    lists = Paginator(posts, 5)
    pages = request.GET.get('page')
    try:
        cons = lists.page(pages)
    except EmptyPage:
        cons = lists.page(lists.num_pages)
    except PageNotAnInteger:
        cons = lists.page(1)

    is_login = request.session.get('is_login')
    if is_login == 'seller':
        name = request.session.get('seller_name')
        user = SellerInfo.objects.get(seller_name=name)
        return render(request, 'index.html', {'name': name, 'cons': cons})
    elif is_login == 'buyer':
        name = request.session.get('buyer_name')
        user = BuyerInfo.objects.get(buyer_name=name)
        return render(request, 'index.html', {'name': name, 'cons': cons})
    else:
        return render(request, 'index.html', {'cons': cons})
