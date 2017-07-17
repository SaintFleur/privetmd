# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Disease,Symptoms,Dataset
from .serializers import DiseaseSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

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

class DiseaseList(APIView):

	def get(self,request):
		disease = Disease.objects.all()
		serializer=DiseaseSerializer(disease,many=True)
		return Response(serializer.data)
















