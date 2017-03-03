from django import forms
from .models import *

class UploadFileForm(forms.Form):
    chromosome = forms.IntegerField()
    gene = forms.CharField()
    results = forms.FileField()

class PatientSearchForm(forms.Form):
    FirstName = forms.CharField(label='First Name', required=False)
    SecondName = forms.CharField(label='Second Name', required=False)

class SampleSearchForm(forms.Form):
    Sequencer = forms.CharField(label='Sequencer', required=False)
    SampleType = forms.CharField(label='Sample Type', required=False)

class InsSearchForm(forms.Form):
    Institution = forms.CharField(label='Institution Name', required=False)
