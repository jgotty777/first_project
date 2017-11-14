"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views
from django.conf.urls import include
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^maternity/', views.maternitySurvey, name='maternity'),
    url(r'^brainSpine/', views.brainSpineSurvey, name='brainSpine'),
    url(r'^emergency/', views.emergencySurvey, name='emergency'),
    url(r'^breastHealth/', views.breastHealthSurvey, name='breastHealth'),
    url(r'^ortho/', views.orthopedicsSurvey, name='orthopedics'),
    url(r'^login_submit/$', views.login_submit, name="login_submit"),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^admin/', admin.site.urls)
]
