from django import forms
from .models import *

class UploadFileForm(forms.Form):
    chromosome = forms.ChoiceField(choices=[(x,x) for x in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,'X','Y']], required=True)
    gene = forms.CharField(required=True)
    results = forms.FileField()
	
class UploadInstForm(forms.Form):
	name = forms.CharField(required=True)
	location = forms.CharField(required=True)
	contactname = forms.CharField(required=True)
	contactemail = forms.EmailField(required=True)
	contactnumber = forms.IntegerField(required=True)
	
	def __init__(self, *args, **kwargs):
		super(UploadInstForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Institution Name"
		self.fields['location'].label = "Institution Location"
		self.fields['contactname'].label = "Contact Name"
		self.fields['contactemail'].label = "Contact Email Address"
		self.fields['contactnumber'].label = "Contact Number"

class PatientSearchForm(forms.Form):
    FirstName = forms.CharField()
    SecondName = forms.CharField()
