from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from core import views
from catalog import views as views_catalog
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^produto/$', views.product, name='product'),
    url(r'^produtos/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', include(admin.site.urls)),
]
