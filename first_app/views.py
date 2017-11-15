# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import User, User_Survey, BSS, BreastHealth, Emergency, Maternity, Orthopedics

# Create page views here.
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


# Create submit views here
def matSubmit(request):
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

def bssSubmit(request):
    pat = User.objects.get(pk=1)
    cond = request.POST.get('bssCondition')
    serv = request.POST.get('bssServices')
    qual = request.POST.get('bssQuality')
    sup = request.POST.get('bssSupportGroup')
    condchange = request.POST.get('bssConditionChange')
    comm = request.POST.get('comments')
    saveObj = BSS(patient_id = pat, condition = cond, service = serv, quality = qual, support = sup, change = condchange, comments = comm)
    saveObj.save()
    return render(request, 'first_app/surveys/submit.html')

def brSubmit(request):
    pat = User.objects.get(pk=1)
    cent = request.POST.get('breastCenter')
    proc = request.POST.get('breastProcedure')
    mamm = request.POST.get('breastMammogram')
    qual = request.POST.get('breastQuality')
    sup = request.POST.get('breastSupportGroup')
    comm = request.POST.get('comments')
    saveObj = BreastHealth(patient_id = pat, center = cent, procedure = proc, mammogram = mamm, quality = qual, support = sup, comments = comm)
    saveObj.save()
    return render(request, 'first_app/surveys/submit.html')

def emergSubmit(request):
    pat = User.objects.get(pk=1)
    cond = request.POST.get('emergCondition')
    cf = request.POST.get('emergCareFlight')
    local = request.POST.get('emergLocal')
    qual = request.POST.get('emergQuality')
    comm = request.POST.get('comments')
    saveObj = Emergency(patient_id = pat, condition = cond, careflight = cf, location = local, quality = qual, comments = comm)
    saveObj.save()
    return render(request, 'first_app/surveys/submit.html')

def orthoSubmit(request):
    pat = User.objects.get(pk=1)
    cond = request.POST.get('orthoCondition')
    treat = request.POST.get('orthoTreatment')
    local = request.POST.get('orthoLocal')
    qual = request.POST.get('orthoQuality')
    comm = request.POST.get('comments')
    saveObj = Orthopedics(patient_id = pat, condition = cond, treatment = treat, location = local, quality = qual, comments = comm)
    saveObj.save()
    return render(request, 'first_app/surveys/submit.html')


# Create Login views here
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

# Create dashboard here
def dashboard(request):
    return render(request, 'first_app/dashboard/dashboard.html')
