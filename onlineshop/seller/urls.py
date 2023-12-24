from django.urls import path
from . import views

urlpatterns = [
    path('seller_log/', views.login, name='seller_login'),
    path('seller_reg/', views.register, name='seller_register'),
    path('def_goods/', views.define_goods, name='goods_definition'),
    path('goods_list/', views.goods_list, name='goods_list'),
    path('good/<int:good_id>/edit/', views.edit_good, name='edit_good'),
    path('log_out/', views.log_out, name='seller_logout'),
]
