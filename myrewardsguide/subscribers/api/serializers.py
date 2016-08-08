from __future__ import absolute_import

from rest_framework import serializers
from rest_framework.response import Response

from subscribers.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = (
            'email',
        )

