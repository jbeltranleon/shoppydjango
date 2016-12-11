from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Product

# Create your views here.

def hello_world(request):
    products = Product.objects.order_by('id')
    template = loader.get_template('index.html')
    title = 'Shoppy - Home'
    context = {
        'products' : products,
        'title' : title
    }
    return HttpResponse(template.render(context, request))
