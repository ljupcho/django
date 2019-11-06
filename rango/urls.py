from django.conf.urls import patterns, url

from rango.controllers import user, about, category, page, search

urlpatterns = patterns('',
						url(r'^$', category.index, name='index'),
						url(r'^add_category/$', category.add, name='add_category'),
						url(r'^category/(?P<category_name_url>\w+)/$', category.show, name='category'),
						url(r'^category/(?P<category_name_url>\w+)/add_page/$', page.add, name='add_page'),
						url(r'^goto/$', page.track_url, name='track_url'),
						url(r'^register/$', user.register, name='register'),
						url(r'^login/', user.attempt_login, name='login'),
						url(r'^logout/', user.attempt_logout, name='logout'),
						url(r'^profile/', user.profile, name='profile'),
						url(r'^other_profiles/', user.other_profiles, name='other_profiles'),
						url(r'^about/', about.show, name='about'),
						url(r'^search/', search.find, name='search'),
						url(r'^like_category/', category.increase_like, name='increase_like'),
						url(r'^suggest_category/$', category.suggest_category, name='suggest_category'),
						url(r'^add_auto_page/$', category.add_auto_page, name='add_auto_page'),
					   )
