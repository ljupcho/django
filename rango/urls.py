from django.conf.urls import patterns, url

from rango.controllers import user, about, category, page

urlpatterns = patterns('',
						url(r'^$', category.index, name='index'),
						url(r'^add_category/$', category.add, name='add_category'),
						url(r'^category/(?P<category_name_url>\w+)/$', category.show, name='category'),
						url(r'^category/(?P<category_name_url>\w+)/add_page/$', page.add, name='add_page'),
						url(r'^register/$', user.register, name='register'),
						url(r'^login/', user.attempt_login, name='login'),
						url(r'^logout/', user.attempt_logout, name='logout'),
						url(r'^about/', about.show, name='about'),
					   )
