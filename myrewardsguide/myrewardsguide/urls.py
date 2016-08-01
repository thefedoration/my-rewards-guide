from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^app', 'myrewardsguide.views.app', name='app'),
    url(r'^cards', include('cards.urls')),
    url(r'^$', 'myrewardsguide.views.home', name='home'),
    url(r'^', 'myrewardsguide.views.handler404', name='404'),
]

# urlpatterns += staticfiles_urlpatterns()
# if settings.DEBUG or settings.TESTING:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
