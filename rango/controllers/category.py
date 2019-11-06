from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
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
		category = Category.objects.get(name__iexact=category_name)
		pages = Page.objects.filter(category=category).order_by('-views')
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


@login_required
def increase_like(request):
	""""
	Increase the number of likes of a category
	"""
	likes = 0
	if request.method == 'GET':
		cat_id = request.GET['category_id']
		category = Category.objects.get(id=int(cat_id))
		if category is not None:
			category.likes = category.likes + 1
			category.save()
			likes = category.likes

	return HttpResponse(likes)


@login_required
def suggest_category(request):
	""""
	Get categories list based on keyword
	"""
	context = RequestContext(request)
	max_results = 5
	categories = []
	if request.method == 'GET':
		suggestion = request.GET['suggestion']
		categories = Category.objects.filter(name__startswith=suggestion)[:max_results]

	return render_to_response('rango/category_list.html', {'cat_list': categories}, context)


@login_required
def add_auto_page(request):
	""""
	From a api search results add the page to the category
	"""
	context = RequestContext(request)
	page = None
	pages = []
	if request.method == 'POST':
		category_id = request.POST['category_id']
		title = request.POST['title']
		url = request.POST['url']
		category = Category.objects.get(id=int(category_id))
		page = Page.objects.get_or_create(category=category, title=title, url=url)
		pages = Page.objects.filter(category=category).order_by('-views')

	return render_to_response('rango/category_list.html', {'pages': pages, 'new_page': page}, context)
