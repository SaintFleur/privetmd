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

# class IsOwnerFilterBackend(filters.BaseFilterBackend):
#     """
#     Filter that only allows users to see their own objects.
#     """
#     def filter_queryset(self, request, queryset, view):
#         return queryset.filter(owner=request.user)


class DatasetList(APIView):
	def get(self,request):
		dataset =Dataset.objects.all()
		serializer = DatasetSerializer(dataset, many=True)
		symptom = self.request.query_params.get('symptom',None)
		if symptom is not None:
			dataset=dataset.filter(symptom=symptom).order_by( '-disease_id' )
			serializer = DatasetSerializer(dataset, many=True)
			print(repr(serializer))
		return Response(serializer.data)











