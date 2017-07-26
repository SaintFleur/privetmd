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
			#try:
			a = row['a']
			b = row['b']
			d = Disease.objects.filter(name=a)
			s = Symptoms.objects.filter(symptom=b)
			#ds = Dataset()
			for i in d: x=i.id
			for i in s: y = print('s',i)
			print(x)

			Disease.objects.get(id=x)
			#for i in s: y= i.id
			#print(x)
			#print()
			#print(.name)
			#print(Symptoms.objects.get(id=y))
			#ds.save()
			#except :
			#	print ('Error',a,b)

	return render(request				, 'index.html')