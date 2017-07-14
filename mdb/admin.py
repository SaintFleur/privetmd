# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Disease,Symptoms,Dataset

# Register your models here.

admin.site.register(Disease)
admin.site.register(Symptoms)
admin.site.register(Dataset)