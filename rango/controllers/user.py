from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.forms import UserForm, UserProfileForm


def register(request):
	"""
	Register new user
	:param request:
	:return:
	"""
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()
			registered = True
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response('rango/register.html',
							  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)


def attempt_login(request):
	"""
	Attempt user login
	:param request:
	:return:
	"""
	context = RequestContext(request)

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/rango/')
			else:
				return HttpResponse("your account is disabled!")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponseForbidden("Invalid login details supplied.")
	else:
		return render_to_response('rango/login.html', {}, context)


@login_required
def attempt_logout(request):
	"""
	Log out the user
	:param request:
	:return:
	"""
	logout(request)

	return HttpResponseRedirect('/rango/')
