from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from . models import *
admin.site.register(Party1, ImportExportModelAdmin)
admin.site.register(statepartyactivate1, ImportExportModelAdmin)
admin.site.register(districtpartyactivate1, ImportExportModelAdmin)
