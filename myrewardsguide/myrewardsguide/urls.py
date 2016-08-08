from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500 #handler400, handler403

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

handler404 = 'myrewardsguide.views.handler404'
handler500 = 'myrewardsguide.views.handler500'

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^cards/', include('cards.urls')),
    url(r'^api/', include('myrewardsguide.api'), name='api'),
    url(r'^app/', 'myrewardsguide.views.app', name='app'),
    url(r'^$', 'myrewardsguide.views.home', name='home'),
    # url(r'^', 'myrewardsguide.views.handler404', name='404'),
]

urlpatterns += staticfiles_urlpatterns()
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
