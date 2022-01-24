from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import *
admin.site.register(Legislative_councils1, ImportExportModelAdmin)
admin.site.register(councilpersonal1, ImportExportModelAdmin)
admin.site.register(councilterm, ImportExportModelAdmin)
