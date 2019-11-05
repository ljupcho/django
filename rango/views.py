from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from rango.forms import CategoryForm, PageForm
from rango.models import Category, Page

def index(request):
	context = RequestContext(request)

	category_list = Category.objects.order_by('-id')[:5]

	# for category in category_list:
	# 	category.url = category.name.replace(' ', '_')

	category_disc = {'categories': category_list}

	return render_to_response('rango/index.html', category_disc, context)

def category(request, category_name_url):
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

def add_category(request):
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

def add_page(request, category_name_url):
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
			return redirect("/rango/category/" + category_name + '/')
		else:
			print form.errors
	else:
		form = PageForm()

	return render_to_response('rango/add_page.html', {'form': form, 'category_name': category_name, 'category_name_url': category_name_url}, context)


def encode_url(str):
    return str.replace(' ', '_')

def decode_url(str):
    return str.replace('_', ' ')