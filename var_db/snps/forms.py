from django import forms
from .models import *

class UploadFileForm(forms.Form):
    chromosome = forms.IntegerField()
    gene = forms.CharField()
    results = forms.FileField()