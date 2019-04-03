from django.shortcuts import render
from django.http import HttpResponse

from index.models import Product
from django.views.generic import ListView
from .form import *


# Create your views here.


def index(request):
    product = ProductForm()
    return render(request, 'data_form.html', context=locals())


def mydate(request, year, month, day):
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


def myyear(request, year):
    return render(request, 'myyear.html')


class ProductList(ListView):
    context_object_name = 'type_list'
    template_name = 'index_view.html'
    queryset = Product.objects.values('type').distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_list'] = Product.objects.values('name', 'type')
        return context
