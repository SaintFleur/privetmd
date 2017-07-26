# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Disease(models.Model):
    name = models.CharField(max_length=200)
    occur = models.IntegerField()
    def publish(self):
        self.save()
    def __str__(self):
        return self.name
class Symptoms(models.Model):
    symptom = models.CharField(max_length=200)
    def publish(self):
        self.save()
    def __str__(self):
        return self.symptom
class Dataset(models.Model):
    disease = models.ForeignKey(Disease)
    symptom = models.ForeignKey(Symptoms)
    def publish(self):
        self.save()
    def __str__(self):
        return str(self.disease.name)
