from __future__ import unicode_literals

from django.db import models

from myrewardsguide.models import BaseModel

# Create your models here.

class Subscriber(BaseModel):
	email = models.EmailField(blank=False, null=False, unique=True)

	def __unicode__(self):
		return '%s' % self.email
	