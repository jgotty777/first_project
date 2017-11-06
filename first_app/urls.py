from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', views.login, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^admin/', admin.site.urls)
]
