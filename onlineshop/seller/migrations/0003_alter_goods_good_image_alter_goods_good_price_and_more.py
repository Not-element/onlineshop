# Generated by Django 4.2.7 on 2023-12-24 07:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_alter_sellerinfo_seller_image_goods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='good_image',
            field=models.ImageField(default='/goods/1b7dcd5357f4f9de52056d36c002ba36.jpg', upload_to='goods', verbose_name='商品图像'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='good_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='商品单价'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='seller',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='seller.sellerinfo'),
        ),
        migrations.AlterField(
            model_name='sellerinfo',
            name='seller_image',
            field=models.ImageField(default='/users/4357443aa53522b.jpg', upload_to='users', verbose_name='用户头像'),
        ),
    ]
