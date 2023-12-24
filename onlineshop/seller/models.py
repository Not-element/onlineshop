from django.core.validators import MinValueValidator
from django.db import models


class SellerInfo(models.Model):
    seller_name = models.CharField(max_length=15)
    seller_image = models.ImageField(upload_to='users', default='/users/4357443aa53522b.jpg', verbose_name='用户头像')
    password = models.CharField(max_length=11)


class Goods(models.Model):
    seller = models.ForeignKey(SellerInfo, default=0, on_delete=models.CASCADE)
    good_name = models.CharField(max_length=15, verbose_name='商品名称')
    good_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品单价',
                                     validators=[MinValueValidator(0)])
    good_state = models.CharField(max_length=10, choices=(('已上架', '已上架'), ('已下架', '已下架')), default='已下架',
                                  verbose_name='商品状态')
    good_image = models.ImageField(upload_to='goods', default='/goods/1b7dcd5357f4f9de52056d36c002ba36.jpg',
                                   verbose_name='商品图像')
    good_info = models.CharField(max_length=50, default='',verbose_name='商品详情')
    good_quantity = models.PositiveIntegerField(verbose_name='库存数量')
    good_label = models.CharField(max_length=10, choices=(('数码', '数码'), ('衣物', '衣物')), default='数码',
                                  verbose_name='商品标签')
