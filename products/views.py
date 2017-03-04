from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from .mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

from django.core.urlresolvers import reverse_lazy

from .models import Product
from .forms import ProductForm

import os
from io import BytesIO
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle, Image

class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    success_url = reverse_lazy('products:home')
    fields = ['name', 'description', 'category', 'price', 'image']
    title = Product.name

class ProductList(ListView):
    model = Product

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product

class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('products:home')
    fields = ['name', 'description', 'category', 'price', 'image']


class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:home')


def reportPDF():
    pass