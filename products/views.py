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
from datetime import date
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


def reportPDF(request):
    products = Product.objects.order_by('id')

    #Create The HttpResponse headers with PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Stock_Report.pdf"'

    #Create the PDF object, using the BytesIO object as it's "file."
    buffer = BytesIO()
    fecha = date.today()
    c = canvas.Canvas(buffer, pagesize=A4)

    #Header
    c.setLineWidth(.3)
    c.setFont('Helvetica', 22)
    c.drawString(30, 750, 'Shoppy')
    c.setFont('Helvetica', 12)
    c.drawString(30, 735, ' Web Store')

    c.setFont('Helvetica-Bold', 12)
    c.drawString(480, 750, fecha.__str__())
    c.line(460,747,560,747)

    #Table Header
    styles = getSampleStyleSheet()
    style_header = styles["Normal"]
    style_header.alignment = TA_CENTER
    style_header.fontSize = 10

    name = Paragraph('''Name''', style_header)
    description = Paragraph('''Description''', style_header)
    category = Paragraph('''Category''', style_header)
    price = Paragraph('''Price''', style_header)

    data = []
    data.append([name, description, category, price])

    #Table Body
    styles = getSampleStyleSheet()
    style_body = styles["BodyText"]
    style_body.alignment =TA_CENTER
    style_body.fontSize = 7

    width, height = A4
    high = 650
    for product in products:
        this_product = [product.name,
                        product.description,
                        product.category,
                        product.price,]
        data.append(this_product)
        high = high -18

    #Table Size
    width, height = A4
    table = Table(data, colWidths=[1.9 * cm,
                                    9.5 * cm,
                                    1.9 * cm,
                                    1.9 * cm,
                                    1.9 * cm,
                                    1.9 * cm,])
    table.setStyle(TableStyle([
        ('INERGRID', (0, 0), (-1, -1), 0.25, colors.black),
        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),]))

    #PDF Size
    table.wrapOn(c, width, height)
    table.drawOn(c, 30, high)
    c.showPage() #Save Page

    #Save PDF
    c.save()

    #Get the value of BytesIO buffer and write response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response