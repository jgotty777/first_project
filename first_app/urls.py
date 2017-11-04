from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [

    url(r'^$', views.index2, name='index2'),
    url(r'^buttsauce/', views.buttsauce, name='buttsauce'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^admin/', admin.site.urls)
]
