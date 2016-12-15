from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.hello_world, name='hello'),
	url(r'^snapchat/', views.snapchat, name='snapchat'),
	url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail')
]