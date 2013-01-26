from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from compare.models import Topic

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$','compareit.views.index'),
    url(r'^', include('compare.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)


    # url(r'^compare/$', 'compare.views.index'),
 #    url(r'^compare/(?P<topic_id>\d+)/$', 'compare.views.detail'),
 #    url(r'^compare/(?P<topic_id>\d+)/results/$', 'compare.views.results'),
 #    url(r'^compare/(?P<topic_id>\d+)/vote/$', 'compare.views.vote'),
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),


