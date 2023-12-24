from django.db import models
from seller.models import Goods
from buyer.models import BuyerInfo


class Order(models.Model):
    buyer = models.ForeignKey(BuyerInfo, on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    state = models.CharField(max_length=10, choices=(('已通过', '已通过'), ('未通过', '未通过')), default='未处理',
                             verbose_name='订单状态')
    date = models.DateTimeField(null=False, blank=False)
    quantity = models.PositiveIntegerField(verbose_name='数目')


# class Cart(models.Model):


class Comment(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE)
    user = models.ForeignKey(BuyerInfo, max_length=100, on_delete=models.CASCADE)
    text = models.TextField(max_length=200, null=False, blank=False)
    create_date = models.DateTimeField(null=False, blank=False)