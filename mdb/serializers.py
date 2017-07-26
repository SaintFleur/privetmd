from rest_framework import serializers
from .models import Disease,Symptoms,Dataset


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields = ('name', 'id')


class DatasetSerializer(serializers.ModelSerializer):

    class Meta:
        model=Dataset
        disease=DiseaseSerializer()
        fields=('disease','symptom')
