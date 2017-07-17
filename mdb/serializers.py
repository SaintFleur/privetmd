from rest_framework import serializers
from .models import Disease,Symptoms,Dataset

class DatasetSerializer(serializers.ModelSerializer):

    class Meta:
        model=Dataset
        fields=('disease',)




