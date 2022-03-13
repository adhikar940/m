from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import *
admin.site.register(Assembly_Constituency1, ImportExportModelAdmin)
admin.site.register(Legislative_Assembly1, ImportExportModelAdmin)
admin.site.register(assemblypersonal1, ImportExportModelAdmin)
admin.site.register(assemblyterm, ImportExportModelAdmin)
admin.site.register(excelupload, ImportExportModelAdmin)
