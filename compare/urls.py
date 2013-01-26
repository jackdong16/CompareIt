from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from compare.models import Topic

from compare import views

urlpatterns = patterns('',
	url(r'^compare/', 'compareit.views.index', name='index'),   
	#url(r'^(?P<topic_id>\d+)/$', 'detail'),
	url(r'^popular/',
    ListView.as_view(
        queryset=Topic.objects.order_by('-pub_date')[:5],
        context_object_name='popular_topics',
        template_name='rank/list.html')),
	url(r'^latest/',
    ListView.as_view(
        queryset=Topic.objects.order_by('-pub_date')[:5],
        context_object_name='popular_topics',
        template_name='rank/list.html')),
)