from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve as serve_static

from core import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contato/$', views.contact, name='contact'),
    url(r'^catalogo/', include('catalog.urls', namespace='catalog')),
    url(r'^admin/', include(admin.site.urls)),
]
