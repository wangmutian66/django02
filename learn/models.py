# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

class fileimg(models.Model):
    filename = models.CharField(max_length=220)

# from django.db import models

# Create your models here.
