from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import State,Districts

admin.site.register(State, ImportExportModelAdmin)
admin.site.register(Districts, ImportExportModelAdmin)