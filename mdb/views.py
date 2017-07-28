# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from .models import Disease,Symptoms,Dataset
from .serializers import DatasetSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import django_filters.rest_framework
import csv
# Create your views here
def index(request):
	if (Disease is not None):
		print('\nEmptying the Database')
		print('_________________________________________________________________')
		delete_everything(Disease)
		delete_everything(Symptoms)
		delete_everything(Dataset)
		print('\nThe Database was successfully emptied')
		print('_________________________________________________________________')
	else:
		print('\nthe Database is empty')
		print('_________________________________________________________________')
		
	with open('data/diseases.csv',encoding='utf8') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	    	a='abc'
	    	b=int(row['b'])
	    	Diseases = Disease()
	    	Diseases.name = row['a']
	    	Diseases.occur = b
	    	Diseases.save()
	print(' \nThe Diseases were successfully uploaded')
	print('_________________________________________________________________')

	
	with open('data/symptoms.csv',encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			a='abc'
			Diseases = Symptoms()
			Diseases.symptom = row['a']
			Diseases.save()
	print('\nThe Symptops were successfully uploaded')
	print('_________________________________________________________________')

	with open('data/dataset.csv', encoding='utf8') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			a = row['a']
			b = row['b']
			d = Disease.objects.filter(name=a)
			s = Symptoms.objects.filter(symptom=b)
			print('Dataset | Processing | Disease: ', d, '| Symptop: ', s)
			ds = Dataset()
			for i in d:
				ds.disease = Disease.objects.get(id=i.id)
			for i in s:
				print(i.id)
				ds.symptom = Symptoms.objects.get(id=i.id)
			ds.save()
	print('\nThe Dataset was successfully created')
	print('_________________________________________________________________')
		
	return render(request, 'index.html')

# class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     """
#     Filter that only allows users to see their own objects.
#     """
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(owner=request.user)

def delete_everything(obj):
    obj.objects.all().delete()

class DatasetList(APIView):
	def get(self,request):
		dataset = Dataset.objects.all()
		serializer = DatasetSerializer(dataset, many=True)
		symptom = self.request.query_params.get('symptom', None)
		if symptom is not None:
			dataset = dataset.filter(symptom=symptom)
			serializer = DatasetSerializer(dataset, many=True)
		return Response(serializer.data)











