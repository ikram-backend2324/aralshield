from django.contrib import admin

from .models import AdviceLog, CitizenReport, District, Snapshot

admin.site.register(District)
admin.site.register(CitizenReport)
admin.site.register(Snapshot)
admin.site.register(AdviceLog)
