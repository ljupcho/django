from django.shortcuts import render_to_response
from django.template import RequestContext


def show(request):
	"""
	Show about page
	:param request:
	:return:
	"""
	context = RequestContext(request)

	return render_to_response('rango/about.html', {'message': "you are in about page"}, context)
