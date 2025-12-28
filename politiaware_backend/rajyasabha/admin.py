from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import *
admin.site.register(Rajyasabhapresedential1, ImportExportModelAdmin)
admin.site.register(Rajyasabha1, ImportExportModelAdmin)
admin.site.register(rajyasabhapersonal1, ImportExportModelAdmin)
admin.site.register(Rajyasabha_Session1, ImportExportModelAdmin)
admin.site.register(Rajyasabha_Complete_Session1, ImportExportModelAdmin)
admin.site.register(Rajyasabhaterm, ImportExportModelAdmin)
