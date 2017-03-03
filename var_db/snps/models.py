from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Variant(models.Model):
    variantid = models.AutoField(primary_key = True)
    chromosome = models.CharField(max_length = 2)
    cdna = models.CharField(max_length = 50, null = True)
    protein = models.CharField(max_length = 50, null = True)
    gdna = models.CharField(max_length = 50, null = True)
    gene = models.CharField(max_length = 50, null = True)
    
    def __str__(self):
        return "%s %s %s %s %s" % (self.chromosome, self.cdna, self.protein, self.gdna, self.gene)

class Institution(models.Model):
    institutionid = models.AutoField(primary_key = True, null = False)
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    contactname = models.CharField(max_length = 50)
    contactnumber = models.IntegerField(null = False) 
    contactemail = models.CharField(max_length = 100)
   
    def __str__(self):
        return "%s %s %s %s %s" % (self.name, self.location, self.contactname, self.contactnumber, self.contactemail)


class Patient(models.Model):
    patientid = models.AutoField(primary_key = True)
    firstname = models.CharField(max_length = 30)
    secondname = models.CharField(max_length = 50) 
    age = models.IntegerField(null = True)
    notes = models.CharField(max_length = 1000)
    institutionid = models.ForeignKey(Institution) 
    
    def __str__(self):
        return "%s %s %s %s" % (self.firstname, self.secondname, self.age, self.notes)



class Samples(models.Model):
    sampleid = models.AutoField(primary_key = True)
    patientid = models.ForeignKey(Patient) 
    sequencer = models.CharField(max_length = 30)
    sampletype = models.CharField(max_length = 30)
   
    def __str__(self):
        return "%s %s %s" % (self.patientid, self.sequencer, self.sampletype)


class Sample2Variant(models.Model):
    sample2variantid = models.AutoField(primary_key = True)
    variantid = models.ForeignKey(Variant) 
    sampleid = models.ForeignKey(Samples) 

    
