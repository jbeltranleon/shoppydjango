from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Product

# Create your views here.

def hello_world(request):
    products = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'products' : products
    }
    return HttpResponse(template.render(context, request))
