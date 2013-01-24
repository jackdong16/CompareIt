from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'compareit.views.home', name='home'),
    #url(r'^compareit/', include('compareit.foo.urls')),
	
	url(r'^$', 'compareit.views.index'),
	url(r'^compare/$', 'compare.views.index'),
    url(r'^compare/(?P<topic_id>\d+)/$', 'compare.views.detail'),
    url(r'^compare/(?P<topic_id>\d+)/results/$', 'compare.views.results'),
    url(r'^compare/(?P<topic_id>\d+)/vote/$', 'compare.views.vote'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
