# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Disease(models.Model):
    name = models.TextField()
   # symptoms = models.TextField()
    occur = models.IntegerField()
    def publish(self):
        self.save()
    def __str__(self):
        return self.name
class Symptoms(models.Model):
    symptom = models.TextField()
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
        return self.name