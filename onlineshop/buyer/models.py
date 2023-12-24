from django.db import models


class BuyerInfo(models.Model):
    buyer_name = models.CharField(max_length=15)
    buyer_image = models.ImageField(upload_to='user', default='/user/4357443aa53522b.jpg', verbose_name='用户头像')
    password = models.CharField(max_length=11)
    email = models.CharField(max_length=25, default='666@qq.com')
