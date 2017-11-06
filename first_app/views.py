# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import Patient, Maternity, Login_User

# Create your views here.
def index(request):
    my_dict = {'insert_me':"Please complete the form below to give Marvel marketing data on which superhero is the favorite of certain demographics. Also from Django"}
    return render(request, 'first_app/assign9/assign9/index.html',context=my_dict)

def submit(request):
    # pat = Patient(pk=1)
    pat = Patient.objects.get(pk=1)
    qual = request.POST.get('deliverySuite')
    freq = request.POST.get('nurse')
    heal = request.POST.get('babyHealth')
    nic = request.POST.get('nicu')
    reas = request.POST.get('nicuCondition')
    comm = request.POST.get('comments')
    saveObj = Maternity(patient_id = pat, quality = qual, frequency = freq, health = heal, nicu = nic, reason = reas, comments = comm)
    saveObj.save()
    return render(request, 'first_app/assign9/assign9/submit.html')

def index2(request):
    return HttpResponse("Stop Judging me")

def buttsauce(request):
    return HttpResponse("<b>buttsauce</b>")

def login(request):
    return render(request, 'first_app/registration/login.html')

def login_submit(request):
    name = request.POST.get('username')
    passw = request.POST.get('password')
    user = Login_User.objects.get(username=name)
    # return HttpResponse(user.admin)
    if user.password == passw:
        if user.admin == 0:
            return render(request, 'first_app/assign9/assign9/index.html')
        if user.admin == 1:
            return render(request, 'first_app/assign9/assign9/dashboard.html')
    else:
        return HttpResponse("Username or Password is incorrect")

def logout(request):
    return HttpResponse("<b>logout</b>")

def dashboard(request):
    return render(request, 'first_app/assign9/assign9/dashboard.html')
