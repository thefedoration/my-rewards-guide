from __future__ import absolute_import

from django.conf.urls import patterns, url, include


urlpatterns = patterns('',
   url(r'^subscribers/', include('subscribers.api.urls')),
)
