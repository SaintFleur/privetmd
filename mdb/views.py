# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Disease,Symptoms,Dataset

import csv
# Create your views here.
def index(request):
	with open('csvfile2.csv', encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:

			a = row['a']
			b = row['b']
			d = Disease.objects.filter(name=a)
			s = Symptoms.objects.filter(symptom=b)
			ds = Dataset()
			for i in d:
				print(i.id)
				ds.disease = Disease.objects.get(id=i.id)
			for i in s:
				print(i.id)
				ds.symptom =Symptoms.objects.get(id=i.id)
			ds.save()

			#print ('Error',a,b)

	return render(request, 'index.html')