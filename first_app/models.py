# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.
from django.db import models

class User(models.Model):
    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    admin = models.IntegerField(default=0)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.CharField(max_length=200)

class User_Survey(models.Model):
    # id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User)
    survey = models.CharField(max_length=100)
    status = models.BooleanField(default=0)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

class Maternity(models.Model):
    # id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User)
    quality = models.IntegerField()
    frequency = models.CharField(max_length=200)
    health = models.CharField(max_length=200)
    nicu = models.BooleanField()
    reason = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

class BSS(models.Model):
    # id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User)
    condition = models.CharField(max_length=200)
    service = models.CharField(max_length=200)
    quality = models.CharField(max_length=200)
    support = models.CharField(max_length=200)
    change = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

class BreastHealth(models.Model):
    # id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User)
    center = models.CharField(max_length=200)
    procedure = models.CharField(max_length=200)
    mammogram = models.CharField(max_length=200)
    quality = models.CharField(max_length=200)
    support = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

class Emergency(models.Model):
    # id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User)
    condition = models.CharField(max_length=200)
    careflight = models.BooleanField()
    location = models.CharField(max_length=200)
    quality = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

class Orthopedics(models.Model):
    # id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(User)
    condition = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    quality = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

