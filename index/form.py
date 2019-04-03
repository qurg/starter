from django import forms
from .models import *


class ProductForm(forms.Form):
    name = forms.CharField(max_length=20, label='Name')
    weight = forms.CharField(max_length=50, label='Weight')
    size = forms.CharField(max_length=50, label='Size')

    choice_list = [(i + 1, v['type_name']) for i, v in enumerate(Type.objects.values('type_name'))]
    type = forms.ChoiceField(choices=choice_list, label='产品类型')
