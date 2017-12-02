# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from .models import User, User_Survey, BSS, BreastHealth, Emergency, Maternity, Orthopedics


# Create page views here.
def index(request):
    return render(request, 'first_app/registration/login.html')


def maternitySurvey(request):
    return render(request, 'first_app/surveys/maternitySurvey.html')


def brainSpineSurvey(request):
    return render(request, 'first_app/surveys/brain_spine_stroke.html')


def emergencySurvey(request):
    return render(request, 'first_app/surveys/emergency.html')


def breastHealthSurvey(request):
    return render(request, 'first_app/surveys/breast_health.html')


def orthopedicsSurvey(request):
    return render(request, 'first_app/surveys/orthopedics.html')


# Create submit views here
def matSubmit(request):
    user_survey_id = request.GET.get('uid')
    user_survey = User_Survey.objects.get(pk=user_survey_id)
    pat = user_survey.patient_id
    qual = request.POST.get('deliverySuite')
    freq = request.POST.get('nurse')
    heal = request.POST.get('babyHealth')
    nic = request.POST.get('nicu')
    reas = request.POST.get('nicuCondition')
    comm = request.POST.get('comments')
    if user_survey.status == 1:
        return HttpResponse("<b>We're sorry, but this survey has already been completed.</b>")
    else:
        user_survey.status = 1
        user_survey.save()
        saveObj = Maternity(patient_id=pat, quality=qual, frequency=freq, health=heal, nicu=nic, reason=reas, comments=comm)
        saveObj.save()

        return render(request, 'first_app/surveys/submit.html')


def bssSubmit(request):
    user_survey_id = request.GET.get('uid')
    user_survey = User_Survey.objects.get(pk=user_survey_id)
    pat = user_survey.patient_id
    cond = request.POST.get('bssCondition')
    serv = request.POST.get('bssServices')
    qual = request.POST.get('bssQuality')
    sup = request.POST.get('bssSupportGroup')
    condchange = request.POST.get('bssConditionChange')
    comm = request.POST.get('comments')
    if user_survey.status == 1:
        return HttpResponse("<b>We're sorry, but this survey has already been completed.</b>")
    else:
        user_survey.status = 1
        user_survey.save()
        saveObj = BSS(patient_id=pat, condition=cond, service=serv, quality=qual, support=sup, change=condchange,
                  comments=comm)
        saveObj.save()
        return render(request, 'first_app/surveys/submit.html')


def brSubmit(request):
    user_survey_id = request.GET.get('uid')
    user_survey = User_Survey.objects.get(pk=user_survey_id)
    pat = user_survey.patient_id
    cent = request.POST.get('breastCenter')
    proc = request.POST.get('breastProcedure')
    mamm = request.POST.get('breastMammogram')
    qual = request.POST.get('breastQuality')
    sup = request.POST.get('breastSupportGroup')
    comm = request.POST.get('comments')
    if user_survey.status == 1:
        return HttpResponse("<b>We're sorry, but this survey has already been completed.</b>")
    else:
        user_survey.status = 1
        user_survey.save()
        saveObj = BreastHealth(patient_id=pat, center=cent, procedure=proc, mammogram=mamm, quality=qual, support=sup,
                           comments=comm)
        saveObj.save()
        return render(request, 'first_app/surveys/submit.html')


def emergSubmit(request):
    user_survey_id = request.GET.get('uid')
    user_survey = User_Survey.objects.get(pk=user_survey_id)
    pat = user_survey.patient_id
    cond = request.POST.get('emergCondition')
    cf = request.POST.get('emergCareFlight')
    local = request.POST.get('emergLocal')
    qual = request.POST.get('emergQuality')
    comm = request.POST.get('comments')
    if user_survey.status == 1:
        return HttpResponse("<b>We're sorry, but this survey has already been completed.</b>")
    else:
        user_survey.status = 1
        user_survey.save()
        saveObj = Emergency(patient_id=pat, condition=cond, careflight=cf, location=local, quality=qual, comments=comm)
        saveObj.save()
        return render(request, 'first_app/surveys/submit.html')


def orthoSubmit(request):
    user_survey_id = request.GET.get('uid')
    user_survey = User_Survey.objects.get(pk=user_survey_id)
    pat = user_survey.patient_id
    cond = request.POST.get('orthoCondition')
    treat = request.POST.get('orthoTreatment')
    local = request.POST.get('orthoLocal')
    qual = request.POST.get('orthoQuality')
    comm = request.POST.get('comments')
    if user_survey.status == 1:
        return HttpResponse("<b>We're sorry, but this survey has already been completed.</b>")
    else:
        user_survey.status = 1
        user_survey.save()
        saveObj = Orthopedics(patient_id=pat, condition=cond, treatment=treat, location=local, quality=qual, comments=comm)
        saveObj.save()
        return render(request, 'first_app/surveys/submit.html')


# Create Login views here
def login_submit(request):
    name = request.POST.get('username')
    passw = request.POST.get('password')
    user = User.objects.get(username=name)
    if user.password == passw:
        if user.admin == 0:
            surveys = User_Survey.objects.filter(patient_id=user, status=0)
            links = []
            for survey in surveys:
                if survey.survey == "Maternity":
                    links.append('maternity')
                elif survey.survey == "Brain":
                    links.append('brainSpine')
                elif survey.survey == "Ortho":
                    links.append('orthopedics')
                elif survey.survey == "Emergency":
                    links.append('emergency')
                elif survey.survey == "Breast":
                    links.append('breastHealth')
            return render(request, 'first_app/dashboard/patient_dashboard.html', {'user': user.pk, 'links': links})
        if user.admin == 1:
            my_dict = {}
            bsss = BSS.objects.all()
            if bsss:
                my_dict['bsss'] = {
                    'condition': {},
                    'service': {},
                    'quality': {},
                    'support': {},
                    'change': {},
                    'comments': [],
                    'total': 0
                }
                total = 0
                for bss in bsss:
                    if not bss.condition in my_dict['bsss']['condition']:
                        my_dict['bsss']['condition'][bss.condition] = 0
                    my_dict['bsss']['condition'][bss.condition] += 1
                    if not bss.service in my_dict['bsss']['service']:
                        my_dict['bsss']['service'][bss.service] = 0
                    my_dict['bsss']['service'][bss.service] += 1
                    if not bss.quality in my_dict['bsss']['quality']:
                        my_dict['bsss']['quality'][bss.quality] = 0
                    my_dict['bsss']['quality'][bss.quality] += 1
                    if not bss.support in my_dict['bsss']['support']:
                        my_dict['bsss']['support'][bss.support] = 0
                    my_dict['bsss']['support'][bss.support] += 1
                    if not bss.change in my_dict['bsss']['change']:
                        my_dict['bsss']['change'][bss.change] = 0
                    my_dict['bsss']['change'][bss.change] += 1
                    if bss.comments:
                        my_dict['bsss']['comments'].append(bss.comments)
                    total += 1
                my_dict['bsss']['total'] = total
                for k, v in my_dict['bsss']['condition'].items():
                    my_dict['bsss']['condition'][k] = round((v/float(my_dict['bsss']['total']))*100, 1)
                for k, v in my_dict['bsss']['service'].items():
                    my_dict['bsss']['service'][k] = round((v/float(my_dict['bsss']['total']))*100, 1)
                for k, v in my_dict['bsss']['quality'].items():
                    my_dict['bsss']['quality'][k] = round((v/float(my_dict['bsss']['total']))*100, 1)
                for k, v in my_dict['bsss']['support'].items():
                    my_dict['bsss']['support'][k] = round((v/float(my_dict['bsss']['total']))*100, 1)
                for k, v in my_dict['bsss']['change'].items():
                    my_dict['bsss']['change'][k] = round((v/float(my_dict['bsss']['total']))*100, 1)

            bhs = BreastHealth.objects.all()
            if bhs:
                my_dict['bhs'] = {
                    'center': {},
                    'procedure': {},
                    'mammogram': {},
                    'quality': {},
                    'support': {},
                    'comments': [],
                    'total': 0
                }
                total = 0
                for bh in bhs:
                    if not bh.center in my_dict['bhs']['center']:
                        my_dict['bhs']['center'][bh.center] = 0
                    my_dict['bhs']['center'][bh.center] += 1
                    if not bh.mammogram in my_dict['bhs']['mammogram']:
                        my_dict['bhs']['mammogram'][bh.mammogram] = 0
                    my_dict['bhs']['mammogram'][bh.mammogram] += 1
                    if not bh.quality in my_dict['bhs']['quality']:
                        my_dict['bhs']['quality'][bh.quality] = 0
                    my_dict['bhs']['quality'][bh.quality] += 1
                    if not bh.support in my_dict['bhs']['support']:
                        my_dict['bhs']['support'][bh.support] = 0
                    my_dict['bhs']['support'][bh.support] += 1
                    if not bh.procedure in my_dict['bhs']['procedure']:
                        my_dict['bhs']['procedure'][bh.procedure] = 0
                    my_dict['bhs']['procedure'][bh.procedure] += 1
                    if bh.comments:
                        my_dict['bhs']['comments'].append(bh.comments)
                    total += 1
                my_dict['bhs']['total'] = total
                for k, v in my_dict['bhs']['center'].items():
                    my_dict['bhs']['center'][k] = round((v/float(my_dict['bhs']['total']))*100, 1)
                for k, v in my_dict['bhs']['procedure'].items():
                    my_dict['bhs']['procedure'][k] = round((v/float(my_dict['bhs']['total']))*100, 1)
                for k, v in my_dict['bhs']['quality'].items():
                    my_dict['bhs']['quality'][k] = round((v/float(my_dict['bhs']['total']))*100, 1)
                for k, v in my_dict['bhs']['support'].items():
                    my_dict['bhs']['support'][k] = round((v/float(my_dict['bhs']['total']))*100, 1)
                for k, v in my_dict['bhs']['mammogram'].items():
                    my_dict['bhs']['mammogram'][k] = round((v/float(my_dict['bhs']['total']))*100, 1)

            es = Emergency.objects.all()

            if es:
                my_dict['es'] = {
                    'condition': {},
                    'careflight': {},
                    'location': {},
                    'quality': {},
                    'comments': [],
                    'total': 0
                }
                total = 0
                for e in es:
                    if not e.condition in my_dict['es']['condition']:
                        my_dict['es']['condition'][e.condition] = 0
                    my_dict['es']['condition'][e.condition] += 1
                    if not e.careflight in my_dict['es']['careflight']:
                        my_dict['es']['careflight'][e.careflight] = 0
                    my_dict['es']['careflight'][e.careflight] += 1
                    if not e.quality in my_dict['es']['quality']:
                        my_dict['es']['quality'][e.quality] = 0
                    my_dict['es']['quality'][e.quality] += 1
                    if not e.location in my_dict['es']['location']:
                        my_dict['es']['location'][e.location] = 0
                    my_dict['es']['location'][e.location] += 1
                    if e.comments:
                        my_dict['es']['comments'].append(e.comments)
                    total += 1
                my_dict['es']['total'] = total
                for k, v in my_dict['es']['condition'].items():
                    my_dict['es']['condition'][k] = round((v/float(my_dict['es']['total']))*100, 1)
                for k, v in my_dict['es']['careflight'].items():
                    my_dict['es']['careflight'][k] = round((v/float(my_dict['es']['total']))*100, 1)
                for k, v in my_dict['es']['quality'].items():
                    my_dict['es']['quality'][k] = round((v/float(my_dict['es']['total']))*100, 1)
                for k, v in my_dict['es']['location'].items():
                    my_dict['es']['location'][k] = round((v/float(my_dict['es']['total']))*100, 1)

            ms = Maternity.objects.all()

            if ms:
                my_dict['ms'] = {
                    'quality': {},
                    'frequency': {},
                    'health': {},
                    'nicu': {},
                    'reason': {},
                    'comments': [],
                    'total': 0
                }
                total = 0
                for m in ms:
                    if not m.frequency in my_dict['ms']['frequency']:
                        my_dict['ms']['frequency'][m.frequency] = 0
                    my_dict['ms']['frequency'][m.frequency] += 1
                    if not m.health in my_dict['ms']['health']:
                        my_dict['ms']['health'][m.health] = 0
                    my_dict['ms']['health'][m.health] += 1
                    if not m.quality in my_dict['ms']['quality']:
                        my_dict['ms']['quality'][m.quality] = 0
                    my_dict['ms']['quality'][m.quality] += 1
                    if not m.nicu in my_dict['ms']['nicu']:
                        my_dict['ms']['nicu'][m.nicu] = 0
                    my_dict['ms']['nicu'][m.nicu] += 1
                    if not m.reason in my_dict['ms']['reason']:
                        my_dict['ms']['reason'][m.reason] = 0
                    my_dict['ms']['reason'][m.reason] += 1
                    if m.comments:
                        my_dict['ms']['comments'].append(m.comments)
                    total += 1
                my_dict['ms']['total'] = total
                for k, v in my_dict['ms']['frequency'].items():
                    my_dict['ms']['frequency'][k] = round((v/float(my_dict['ms']['total']))*100, 1)
                for k, v in my_dict['ms']['health'].items():
                    my_dict['ms']['health'][k] = round((v/float(my_dict['ms']['total']))*100, 1)
                for k, v in my_dict['ms']['quality'].items():
                    my_dict['ms']['quality'][k] = round((v/float(my_dict['ms']['total']))*100, 1)
                for k, v in my_dict['ms']['nicu'].items():
                    my_dict['ms']['nicu'][k] = round((v/float(my_dict['ms']['total']))*100, 1)
                for k, v in my_dict['ms']['reason'].items():
                    my_dict['ms']['reason'][k] = round((v/float(my_dict['ms']['total']))*100, 1)

            os = Orthopedics.objects.all()
            if os:
                my_dict['os'] = {
                    'condition': {},
                    'treatment': {},
                    'location': {},
                    'quality': {},
                    'comments': []
                }
                total = 0
                for o in os:
                    if not o.condition in my_dict['os']['condition']:
                        my_dict['os']['condition'][o.condition] = 0
                    my_dict['os']['condition'][o.condition] += 1
                    if not o.treatment in my_dict['os']['treatment']:
                        my_dict['os']['treatment'][o.treatment] = 0
                    my_dict['os']['treatment'][o.treatment] += 1
                    if not o.quality in my_dict['os']['quality']:
                        my_dict['os']['quality'][o.quality] = 0
                    my_dict['os']['quality'][o.quality] += 1
                    if not o.location in my_dict['os']['location']:
                        my_dict['os']['location'][o.location] = 0
                    my_dict['os']['location'][o.location] += 1
                    if o.comments:
                        my_dict['os']['comments'].append(o.comments)
                    total += 1
                my_dict['os']['total'] = total
                for k, v in my_dict['os']['condition'].items():
                    my_dict['os']['condition'][k] = round((v/float(my_dict['os']['total']))*100, 1)
                for k, v in my_dict['os']['treatment'].items():
                    my_dict['os']['treatment'][k] = round((v/float(my_dict['os']['total']))*100, 1)
                for k, v in my_dict['os']['quality'].items():
                    my_dict['os']['quality'][k] = round((v/float(my_dict['os']['total']))*100, 1)
                for k, v in my_dict['os']['location'].items():
                    my_dict['os']['location'][k] = round((v/float(my_dict['os']['total']))*100, 1)

            return render(request, 'first_app/dashboard/dashboard.html', context=my_dict)
    else:
        return HttpResponse("Username or Password is incorrect")


def logout(request):
    return HttpResponse("<b>logout</b>")


# Create dashboard here
def dashboard(request):
    return render(request, 'first_app/dashboard/dashboard.html')
