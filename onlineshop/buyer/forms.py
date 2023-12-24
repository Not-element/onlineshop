from django import forms
from . import models


class BuyerInfoForm(forms.ModelForm):

    class Meta:
        model = models.BuyerInfo
        fields = ['buyer_name', 'buyer_image', 'password', 'email']
