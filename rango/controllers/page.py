from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from rango.forms import PageForm
from rango.models import Category


@login_required
def add(request, category_name_url):
	"""
	Handle save of Category
	"""
	context = RequestContext(request)
	category_name = decode_url(category_name_url)
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			page = form.save(commit=False)
			cat = Category.objects.get(name=category_name)
			page.category = cat
			page.views = 0
			page.save()

			# return category(request, category_name_url)
			#: shouldn't really render the view here, rather it should do a redirect
			# return redirect("/rango/category/" + category_name + '/')
			return HttpResponseRedirect("/rango/category/" + category_name + '/')
		else:
			print form.errors
	else:
		form = PageForm()

	return render_to_response('rango/add_page.html',
							  {'form': form, 'category_name': category_name, 'category_name_url': category_name_url},
							  context)


def encode_url(str):
	return str.replace(' ', '_')


def decode_url(str):
	return str.replace('_', ' ')
