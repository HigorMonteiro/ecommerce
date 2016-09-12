from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from core import views
admin.autodiscover()

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^produto/$', views.product, name='product'),
    url(r'^produtos/$', views.product_list, name='product_list'),
    url(r'^admin/', include(admin.site.urls)),
]
