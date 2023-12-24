# Generated by Django 4.2.7 on 2023-12-24 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerinfo',
            name='seller_image',
            field=models.ImageField(default='/seller/4357443aa53522b.jpg', upload_to='seller', verbose_name='用户头像'),
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_name', models.CharField(max_length=15, verbose_name='商品名称')),
                ('good_price', models.PositiveIntegerField(verbose_name='商品单价')),
                ('good_state', models.CharField(choices=[('已上架', '已上架'), ('已下架', '已下架')], default='已下架', max_length=10, verbose_name='商品状态')),
                ('good_image', models.ImageField(default='/seller/1b7dcd5357f4f9de52056d36c002ba36.jpg', upload_to='seller', verbose_name='商品图像')),
                ('good_info', models.CharField(default='', max_length=50, verbose_name='商品详情')),
                ('good_quantity', models.PositiveIntegerField(verbose_name='库存数量')),
                ('good_label', models.CharField(choices=[('数码', '数码'), ('衣物', '衣物')], default='数码', max_length=10, verbose_name='商品标签')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.sellerinfo')),
            ],
        ),
    ]
