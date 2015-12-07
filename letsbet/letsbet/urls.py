from django.conf.urls import include, url
from django.contrib import admin
import csgorox.settings as settings
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'letsbet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^deposit/', views.view_that_asks_for_money, name='view_that_asks_for_money'),
    url(r'^something/', include('paypal.standard.ipn.urls')),
]
