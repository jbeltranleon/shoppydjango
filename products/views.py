from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView

from django.core.urlresolvers import reverse_lazy

from .models import Product
from .forms import ProductForm

# Create your views here.

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy('products:home')
    fields = ['name', 'description', 'category', 'price', 'image']

class ProductList(ListView):
    model = Product

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product