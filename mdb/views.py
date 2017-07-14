# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Disease
import csv
# Create your views here.
def index(request):
	import csv
	with open('2.csv',encoding='utf8') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	    	a='abc'
	    	b=int(row['b'])
	    	Diseases = Disease()
	    	Diseases.name = row['a']
	    	Diseases.occur = b
	    	Diseases.save()
	return render(request, 'index.html')
