from django.contrib import admin

from subscribers.models import Subscriber

# Register your models here.
class SubscriberAdmin(admin.ModelAdmin):
    model = Subscriber
    list_display = ('email', 'datetime_created',)

admin.site.register(Subscriber, SubscriberAdmin)