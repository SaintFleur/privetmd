# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Disease,Symptoms
import csv
# Create your views here.
def index(request):
	# import csv
	# with open('symptoms.csv',encoding='utf8') as csvfile:
	#     reader = csv.DictReader(csvfile)
	#     for row in reader:
	#     	a='abc'
	#     	#b=int(row['b'])
	#     	Diseases = Symptoms()
	#     	Diseases.symptom = row['a']
	#     	Diseases.save()
	return render(request, 'index.html')
