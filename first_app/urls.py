from django.conf.urls import url
from first_app import views

urlpatterns = [

    url(r'^$', views.index2, name='index2'),
    url(r'^buttsauce/', views.buttsauce, name='buttsauce')
    
]
