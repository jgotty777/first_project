# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import User, Maternity, User_Survey

# Create your views here.
def index(request):
    return render(request, 'first_app/registration/login.html')

def maternitySurvey(request):
     my_dict = {'insert_me':"Please complete the form below to give Marvel marketing data on which superhero is the favorite of certain demographics. Also from Django"}
     return render(request, 'first_app/surveys/maternitySurvey.html',context=my_dict)


def brainSpineSurvey(request):
    my_dict = {
        'insert_me': "Please complete the form below to give Marvel marketing data on which superhero is the favorite of certain demographics. Also from Django"}
    return render(request, 'first_app/surveys/maternitySurvey.html', context=my_dict)

def emergencySurvey(request):
    my_dict = {
        'insert_me': "Please complete the form below to give Marvel marketing data on which superhero is the favorite of certain demographics. Also from Django"}
    return render(request, 'first_app/surveys/emergency.html', context=my_dict)

def breastHealthSurvey(request):
    my_dict = {
        'insert_me': "Please complete the form below to give Marvel marketing data on which superhero is the favorite of certain demographics. Also from Django"}
    return render(request, 'first_app/surveys/breast_health.html', context=my_dict)

def orthopedicsSurvey(request):
    my_dict = {
        'insert_me': "Please complete the form below to give Marvel marketing data on which superhero is the favorite of certain demographics. Also from Django"}
    return render(request, 'first_app/surveys/orthopedics.html', context=my_dict)

def submit(request):
    pat = User.objects.get(pk=1)
    qual = request.POST.get('deliverySuite')
    freq = request.POST.get('nurse')
    heal = request.POST.get('babyHealth')
    nic = request.POST.get('nicu')
    reas = request.POST.get('nicuCondition')
    comm = request.POST.get('comments')
    saveObj = Maternity(patient_id = pat, quality = qual, frequency = freq, health = heal, nicu = nic, reason = reas, comments = comm)
    saveObj.save()
    return render(request, 'first_app/surveys/submit.html')

def login_submit(request):
    name = request.POST.get('username')
    passw = request.POST.get('password')
    user = User.objects.get(username=name)
    if user.password == passw:
        if user.admin == 0:
            if user.survey == "Maternity":
                return render(request, 'first_app/surveys/maternitySurvey.html')
            if user.survey == "Brain":
                return render(request, 'first_app/surveys/brain_spine_stroke.html')
            if user.survey == "Ortho":
                return render(request, 'first_app/surveys/orthopedics.html')
            if user.survey == "Emergency":
                return render(request, 'first_app/surveys/emergency.html')
            if user.survey == "Breast":
                return render(request, 'first_app/surveys/breast_health.html')
            else:
                return HttpResponse("No Survey Found")
        if user.admin == 1:
            return render(request, 'first_app/dashboard/dashboard.html')
    else:
        return HttpResponse("Username or Password is incorrect")

def logout(request):
    return HttpResponse("<b>logout</b>")

def dashboard(request):
    return render(request, 'first_app/dashboard/dashboard.html')
