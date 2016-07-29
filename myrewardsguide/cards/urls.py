from django.conf.urls import patterns, include, url

urlpatterns = patterns('cards.views',
   	url(r'^', 'cards'),
)

