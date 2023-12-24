import re
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import BuyerInfoForm
from .models import BuyerInfo


def register(request):
    is_login = request.session.get('is_login')
    if is_login == 'buyer':
        buyer_name = request.session.get('buyer_name')
        buyer = BuyerInfo.objects.get(buyer_name=buyer_name)
        buyer_image_url = buyer.buyer_image.url
        return render(request, 'index.html', {'name': buyer_name, 'image_url': buyer_image_url})
    else:
        if request.method == 'GET':
            form = BuyerInfoForm()
            return render(request, 'buyer_register.html', {'form': form})
        else:
            form = BuyerInfoForm(request.POST, request.FILES)

            def validate_email(value):
                pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
                if not re.match(pattern, value):
                    raise ValidationError('邮箱格式错误')

            try:
                if form.is_valid():
                    buyer = form.save(commit=False)
                    image = request.FILES.get('buyer_image')
                    if image:
                        buyer.buyer_image = image
                    validate_email(form.cleaned_data['email'])
                    buyer.save()
                    return render(request, 'buyer_login.html', {'tip': '请登录'})
                else:
                    return render(request, 'buyer_register.html', {'form': form, 'tip': '请输入数据'})
            except ValidationError:
                return render(request, 'buyer_register.html', {'form': form, 'tip': '邮箱格式错误'})


def login(request):
    is_login = request.session.get('is_login')
    if is_login == 'buyer':
        buyer_name = request.session.get('buyer_name')
        buyer = BuyerInfo.objects.get(buyer_name=buyer_name)
        buyer_image_url = buyer.buyer_image.url
        return render(request, 'index.html', {'name': buyer_name, 'image_url': buyer_image_url})
    else:
        if request.method == 'GET':
            return render(request, 'buyer_login.html')
        else:
            buyer_name = request.POST.get('buyer')
            password = request.POST.get('pwd')
            if not BuyerInfo.objects.filter(buyer_name=buyer_name).exists():
                return render(request, 'buyer_login.html', {'tip': '用户名不存在'})
            else:
                user = BuyerInfo.objects.get(buyer_name=buyer_name)
                if password == user.password:
                    request.session['is_login'] = 'buyer'
                    request.session['buyer_name'] = buyer_name
                    return render(request, 'index.html', {'is_login': 'buyer', 'name': buyer_name})
                else:
                    return render(request, 'buyer_login.html', {'tip': '密码错误'})


def log_out(request):
    request.session.flush()
    return redirect('/index/')
