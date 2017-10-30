# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me':"Please complete the form below to give Marvel marketing data on which superhero is the favorite of certain demographics. Also from Django"}
    return render(request, 'first_app/assign9/assign9/index.html',context=my_dict)

def submit(request):
    return HttpResponse(request, 'first_app/assign9/assign9/submit.html')

def index2(request):
    return HttpResponse("Stop Judging me")

def buttsauce(request):
    return HttpResponse("<b>buttsauce</b>")
