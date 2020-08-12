from django.shortcuts import render, redirect
from . forms import RegisterForm, UserProfileForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if form.is_valid() and profile_form.is_valid():

			user = form.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			profile.save()

			user_name = form.cleaned_data['username']
			user_email = form.cleaned_data['email']

			template = render_to_string('account/email_template.html', {'name': user_name})

			email = EmailMessage(
					'Welcome To Printweza',
					template,
					settings.EMAIL_HOST_USER,
					[user_email]
				)

			email.fail_silently=False
			email.send()

			messages.success(request, 'Your Account has been created successfully. You can now login')
			return redirect('login')

	else:

		form = RegisterForm()
		profile_form = UserProfileForm()

	return render(request, 'account/register.html', {'form': form, 'profile_form': profile_form})
