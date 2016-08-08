
# from __future__ import absolute_import
from django.conf.urls import patterns, include, url
from rest_framework import routers

from subscribers.api.views import SubscriberViewSet



router = routers.SimpleRouter()
router.register(r'subscribers', SubscriberViewSet, 'Subscriber')

urlpatterns = router.urls
