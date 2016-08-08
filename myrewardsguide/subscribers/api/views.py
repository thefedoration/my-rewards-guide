from __future__ import absolute_import

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework import viewsets
from rest_framework import mixins


from subscribers.models import Subscriber

from subscribers.api.serializers import SubscriberSerializer


class SubscriberViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):

	model = Subscriber

	def get_serializer_class(self, *args, **kwargs):
		return SubscriberSerializer


