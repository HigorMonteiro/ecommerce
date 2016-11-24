# coding=utf-8

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        r'^carrinho/adicionar/(?P<slug>[\w_-]+)/$', views.create_cartitem,
        name='create_cartitem'
    ),
    url(r'^carrinho/$', views.cart_item, name='cart_item')
]
