from django.shortcuts import render, redirect
from .models import SellerInfo, Goods
from .forms import GoodsForm


def register(request):
    is_login = request.session.get('is_login')
    if is_login == 'seller':
        seller_name = request.session.get('seller_name')
        seller = SellerInfo.objects.get(seller_name=seller_name)
        seller_image_url = seller.seller_image.url
        return render(request, 'index.html', {'name': seller_name, 'is_login': 'seller',
                                              'image_url': seller_image_url})
    else:
        if request.method == 'GET':
            return render(request, 'seller_register.html')
        else:
            seller_name = request.POST.get('seller')
            password = request.POST.get('pwd')
            re_password = request.POST.get('rpwd')
            if password != re_password:
                return render(request, 'seller_register.html', {'tip': '两次密码输入不同'})
            elif 0 < len(seller_name) < 3 or len(seller_name) > 15:
                return render(request, 'seller_register.html', {'tip': '用户名长度应在3到5之间'})
            elif 0 < len(password) < 3 or len(password) > 10:
                return render(request, 'seller_register.html', {'tip': '密码长度应在3到10之间'})
            elif password == re_password:
                if not SellerInfo.objects.filter(seller_name=seller_name).exists():
                    seller = SellerInfo(seller_name=seller_name, password=password)
                    seller.save()
                    return render(request, 'seller_login.html', {'tip': '注册成功,请登录'})
                else:
                    return render(request, 'seller_register.html', {'tip': '用户名存在'})


def login(request):
    is_login = request.session.get('is_login')
    if is_login == 'seller':
        seller_name = request.session.get('seller_name')
        seller = SellerInfo.objects.get(seller_name=seller_name)
        seller_image_url = seller.seller_image.url
        return render(request, 'index.html', {'name': seller_name, 'is_login': 'seller',
                                              'image_url': seller_image_url})
    else:
        if request.method == 'GET':
            return render(request, 'seller_login.html')
        else:
            seller_name = request.POST.get('seller')
            password = request.POST.get('pwd')
            if not SellerInfo.objects.filter(seller_name=seller_name).exists():
                return render(request, 'seller_login.html', {'tip': '用户名不存在'})
            else:
                user = SellerInfo.objects.get(seller_name=seller_name)
                if password == user.password:
                    request.session['is_login'] = 'seller'
                    request.session['seller_name'] = seller_name
                    request.session['seller_id'] = user.id
                    return render(request, 'index.html', {'name': seller_name, 'is_login': 'seller'})
                else:
                    return render(request, 'seller_login.html', {'tip': '密码错误'})


def log_out(request):
    request.session.flush()
    return redirect('/index/')


def define_goods(request):  # 定义商品信息，模型Goods
    if request.method == 'GET':
        form = GoodsForm()
        return render(request, 'goods_definition.html', {'form': form})
    elif request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            good = form.save(commit=False)
            image = request.FILES.get('good_image')
            if image:
                good.good_image = image
            seller_name = request.session.get('seller_name')
            seller = SellerInfo.objects.get(seller_name=seller_name)

            # 检查商户名下是否存在同名商品
            existing_goods = Goods.objects.filter(seller=seller, good_name=good.good_name).exclude(id=good.id)
            if existing_goods:
                return render(request, 'goods_definition.html',
                              {'form': form, 'tip': '该商户已有同名商品，请修改商品名称'})

            good.seller = seller
            good.save()
            return render(request, 'goods_definition.html', {'form': form, 'tip': '保存成功'})
        else:
            return render(request, 'goods_definition.html', {'form': form, 'tip': '请输入数据'})


def goods_list(request):
    seller_name = request.session.get('seller_name')
    seller = SellerInfo.objects.get(seller_name=seller_name)
    goods = Goods.objects.filter(seller=seller)
    return render(request, 'seller_goods_list.html', {'goods': goods})


def edit_good(request, good_id):  # 修改商品信息
    good = Goods.objects.get(id=good_id)
    good_state_choices = Goods._meta.get_field('good_state').choices
    if request.method == 'POST':
        good_name = request.POST.get('good_name')
        good_price = request.POST.get('good_price')
        good_quantity = request.POST.get('good_quantity')
        good_label = request.POST.get('good_label')
        good_state = request.POST.get('good_state')
        good.good_name = good_name
        good.good_price = good_price
        good.good_quantity = good_quantity
        good.good_label = good_label
        good.good_state = good_state
        good.save()
        return redirect('goods_list')
    return render(request, 'edit_good.html', {'good': good,
                                              'good_state_choices': good_state_choices})
