from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.forms import CategoryForm
from rango.models import Category, Page


def index(request):
	"""
	List categories
	:param request:
	:return:
	"""
	context = RequestContext(request)

	category_list = Category.objects.order_by('-id')[:5]

	category_disc = {'categories': category_list}

	return render_to_response('rango/index.html', category_disc, context)


def show(request, category_name_url):
	"""
	Show details about Category
	:param request:
	:param category_name_url:
	:return:
	"""
	context = RequestContext(request)

	category_name = category_name_url.replace("_", " ")

	context_dict = {'category_name': category_name}

	try:
		category = Category.objects.get(name=category_name)
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass

	return render_to_response('rango/category.html', context_dict, context)


@login_required
def add(request):
	"""
	Handle sasve of Category
	:param request:
	:return:
	"""
	context = RequestContext(request)
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)

			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm()

	return render_to_response('rango/add_category.html', {'form': form}, context)
