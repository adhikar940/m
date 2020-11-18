from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(Movie, ImportExportModelAdmin)

admin.site.register(BiharCandidate, ImportExportModelAdmin)

admin.site.register(BiharWinners, ImportExportModelAdmin)

admin.site.register(BiharRunners, ImportExportModelAdmin)

admin.site.register(DubbakaCandidate, ImportExportModelAdmin)

admin.site.register(DubbakaWinners, ImportExportModelAdmin)

admin.site.register(DubbakaRunners, ImportExportModelAdmin)

admin.site.register(Bihar_Coalition_Party, ImportExportModelAdmin)

admin.site.register(Party, ImportExportModelAdmin)

admin.site.register(States, ImportExportModelAdmin)

admin.site.register(LeadingSeats, ImportExportModelAdmin)

admin.site.register(Rajyasabha, ImportExportModelAdmin)

admin.site.register(LokSabha, ImportExportModelAdmin)

admin.site.register(Assembly_time_period, ImportExportModelAdmin)

admin.site.register(Panchayat_time_period, ImportExportModelAdmin)

admin.site.register(Municipal_corporation_time_period, ImportExportModelAdmin)


