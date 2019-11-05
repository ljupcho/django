from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.bing_search import run_query


def find(request):
	context = RequestContext(request)
	result = []

	if request.method == 'POST':
		query = request.POST['query'].strip()
		if query:
			result = run_query(query)

	return render_to_response('rango/search.html', {'result_list': result}, context)