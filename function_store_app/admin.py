from django.contrib import admin
from .models import *

@admin.register(FunctionDefinition)
class FunctionDefinitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
