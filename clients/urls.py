from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^login', views.authentication, name='authentication'),
	url(r'^registered/$', views.registered, name='registered')
]