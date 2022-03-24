from django.contrib import admin
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin
from . models import *
from import_export import resources

class Assembly_Constituency1Resource(resources.ModelResource):
    class Meta:
        model = Assembly_Constituency1
class Assembly_Constituency1Admin(ImportExportModelAdmin):
    #list_display=('MLA_name',)
    list_filter=('State',)
    resource_class = Assembly_Constituency1Resource
admin.site.register(Assembly_Constituency1, Assembly_Constituency1Admin)

#admin.site.register(Legislative_Assembly1, ImportExportModelAdmin)
class Legislative_Assembly1Resource(resources.ModelResource):
    class Meta:
        model = Legislative_Assembly1
class Legislative_Assembly1Admin(ImportExportModelAdmin):
    #list_display=('MLA_name',)
    list_filter=('state','Party')
    resource_class = Legislative_Assembly1Resource
admin.site.register(Legislative_Assembly1, Legislative_Assembly1Admin)

admin.site.register(assemblypersonal1, ImportExportModelAdmin)
admin.site.register(assemblyterm, ImportExportModelAdmin)
admin.site.register(excelupload, ImportExportModelAdmin)
