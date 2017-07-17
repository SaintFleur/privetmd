from rest_framework import serializers
from .models import Disease,Symptoms,Dataset

class DiseaseSerializer(serializers.ModelSerializer):

    class Meta:
        model= Disease
        fields=('name','occur',)




