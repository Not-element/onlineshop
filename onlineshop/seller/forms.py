from django import forms
from .models import SellerInfo, Goods


class SellerInfoForm(forms.ModelForm):

    class Meta:
        model = SellerInfo
        fields = ['seller_name', 'seller_image', 'password']


class GoodsForm(forms.ModelForm):

    class Meta:
        model = Goods
        fields = ['seller', 'good_name', 'good_price', 'good_label', 'good_quantity', 'good_image']
