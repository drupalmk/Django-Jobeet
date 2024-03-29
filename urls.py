from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from jobs.models import Jobs, Categories
admin.site.register(Jobs)
admin.site.register(Categories)

import settings

urlpatterns = patterns('',  
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    url(r'^$', 'jobs.views.index', name='front'),
    url(r'^jobs/$', 'jobs.views.index', name='jobs'),
    url(r'^jobs/(?P<company>[-\w]+)/(?P<id>\d+)/(?P<position>[-\w]+)/(?P<location>[-\w]+)/$', 'jobs.views.show_job', name="front_jobs"),
    #url(r'^jobs/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    #url(r'^jobs/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    # Examples:
    # url(r'^$', 'jobeet.views.home', name='home'),
    # url(r'^jobeet/', include('jobeet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
