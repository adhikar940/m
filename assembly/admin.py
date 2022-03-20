from django.contrib import admin
from import_export.admin import ImportExportModelAdmin,ImportExportActionModelAdmin
from . models import *
from import_export import resources
admin.site.register(Assembly_Constituency1, ImportExportModelAdmin)
#admin.site.register(Legislative_Assembly1, ImportExportModelAdmin)
class Legislative_Assembly1Resource(resources.ModelResource):
    class Meta:
        model = Legislative_Assembly1
class Legislative_Assembly1Admin(ImportExportModelAdmin):
    #list_display=('MLA_name',)
    list_filter=('state','Party')
    resource_class = Legislative_Assembly1Resource
'''class Legislative_Assembly1Admin(ImportExportActionModelAdmin):
    pass'''
admin.site.register(Legislative_Assembly1, Legislative_Assembly1Admin)
admin.site.register(assemblypersonal1, ImportExportModelAdmin)
admin.site.register(assemblyterm, ImportExportModelAdmin)
admin.site.register(excelupload, ImportExportModelAdmin)
