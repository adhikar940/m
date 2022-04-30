from django.contrib import admin
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin
from . models import *
from import_export import resources
class Legislative_councils1Resource(resources.ModelResource):
    class Meta:
        model = Legislative_councils1
class Legislative_councils1Admin(ImportExportModelAdmin):
    list_display=('MLC_name',)
    search_fields = ['id','Districts']
    list_filter=('state',)
    resource_class = Legislative_councils1Resource
admin.site.register(Legislative_councils1, Legislative_councils1Admin)

#admin.site.register(Legislative_councils1, ImportExportModelAdmin)
admin.site.register(councilpersonal1, ImportExportModelAdmin)
admin.site.register(councilterm, ImportExportModelAdmin)
