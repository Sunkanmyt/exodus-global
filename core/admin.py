from django.contrib import admin
from .models import Sermon, Event, Milestone, ContactMessage, Partnertier, Partner, MinistryInfo

admin.site.register(Sermon)
admin.site.register(Event)
admin.site.register(Milestone)
admin.site.register(ContactMessage)
admin.site.register(Partnertier)
admin.site.register(Partner)
admin.site.register(MinistryInfo)
