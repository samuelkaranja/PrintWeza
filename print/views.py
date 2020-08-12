from django.shortcuts import render, redirect
from . models import *
from . forms import ContactForm, DocumentForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def index(request):
	form = ContactForm()

	if request.method == 'POST':
		form = ContactForm(request.POST)

		if form.is_valid():
			contact_name = form.cleaned_data['name']
			contact_email = form.cleaned_data['email']
			contact_message = form.cleaned_data['message']

		template = render_to_string('print/email_template.html', {'name': contact_name})

		email = EmailMessage(
				'Thank you',
				template,
				settings.EMAIL_HOST_USER,
				[contact_email]
			)

		email.fail_silently=False
		email.send()

	return render(request, 'print/index.html', {'form':form})

@login_required(login_url='login')
def print(request):
	doc = Document.objects.all()
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES, initial = {'user': request.user})
		if form.is_valid():
			instance = form.save(commit=False)
			instance.user = request.user
			instance.save()
			return redirect('job')
	else:
		form = DocumentForm()
	return render(request, 'print/print.html', {'form': form, 'doc':doc})

def job(request):
	document = Document.objects.filter(user=request.user)

	return render(request, 'print/jobs.html', {'document':document})

def preview(request, pk):
	document1 = Document.objects.filter(pk=pk)
	document2 = Document.objects.filter(user=request.user)

	doc = document1 & document2

	return render(request, 'print/preview.html', {'doc': doc})

def updateDocument(request, pk):
	document = Document.objects.get(id=pk)
	
	form = DocumentForm(instance=document)

	if request.method == 'POST':
		form = DocumentForm(request.POST, instance=document)
		if form.is_valid():
			form.save()
			return redirect('preview')
	
	return render(request, 'print/print.html', {'form': form, 'document':document})

def total(request, pk):

	document = Document.objects.get(pk=pk)

	return render(request, 'print/total.html', {'document': document})

def done(request):
	return render(request, 'print/done.html')

def condition(request):
	return render(request, 'print/conditions.html')

def policy(request):
	return render(request, 'print/policy.html')

