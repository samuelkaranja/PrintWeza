from django import forms
from django.forms import ModelForm
from . models import Contact, Document

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		fields = '__all__'