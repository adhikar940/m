from django.contrib import admin
from . models import *
from import_export.admin import ImportExportModelAdmin
'''class flagAdmin(admin.ModelAdmin):
    search_fields = ('color',)
admin.site.register(flag,flagAdmin)'''
admin.site.register(flag, ImportExportModelAdmin)
'''class flag1Admin(admin.ModelAdmin):
    search_fields = ('name',)
admin.site.register(flag1,flag1Admin)'''
admin.site.register(flag1, ImportExportModelAdmin)
