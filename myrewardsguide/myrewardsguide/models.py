from __future__ import unicode_literals

from django.db import models

# Create your models here.
class BaseModel(models.Model):

    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True