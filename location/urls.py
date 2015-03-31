from django.conf.urls import patterns, url
from location import views

urlpatterns = patterns('',
	#url(r'^$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
	url(r'^(?P<phone_id>\d+)/update/$', views.update, name='update'),
)