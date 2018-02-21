from django.contrib import admin
from .models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp']

    class Meta:
        model = Notification

admin.site.register(Notification, NotificationAdmin)
