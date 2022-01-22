from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *
#from loksabha.models import Loksabha_Complete_Session
admin.site.register(PartyMemberPassword, ImportExportModelAdmin)

admin.site.register(PartywiseMP, ImportExportModelAdmin)

admin.site.register(PartywiseMLA, ImportExportModelAdmin)

admin.site.register(States, ImportExportModelAdmin)

admin.site.register(Rajyasabha_Session, ImportExportModelAdmin)

admin.site.register(Legislative_Assembly_Session, ImportExportModelAdmin)

admin.site.register(Legislative_council_Session, ImportExportModelAdmin)

admin.site.register(user_profile, ImportExportModelAdmin)

##### Party
admin.site.register(Party, ImportExportModelAdmin)
class partyAdmin(admin.ModelAdmin):
    search_fields = ('party',)
admin.site.register(statepartyactivate,partyAdmin)
#admin.site.register(statepartyactivate, ImportExportModelAdmin)

##### Rajyasabha
class rajyasabhaAdmin(admin.ModelAdmin):
    search_fields = ('MP_name',)
admin.site.register(Rajyasabha,rajyasabhaAdmin)
#admin.site.register(Rajyasabha, ImportExportModelAdmin)
class rajyasabhapersonalAdmin(admin.ModelAdmin):
    search_fields = ('mp',)
admin.site.register(rajyasabhapersonal, rajyasabhapersonalAdmin)
admin.site.register(Rajyasabhapresedential, ImportExportModelAdmin)
##### Loksabha
class loksabhaAdmin(admin.ModelAdmin):
    search_fields = ('MP_name',)
admin.site.register(LokSabha,loksabhaAdmin)
#admin.site.register(LokSabha, ImportExportModelAdmin)
admin.site.register(Loksabha_Session, ImportExportModelAdmin)
class loksabhapersonalAdmin(admin.ModelAdmin):
    search_fields = ('mp',)
admin.site.register(loksabhapersonal, loksabhapersonalAdmin)
admin.site.register(Loksabha_Complete_Session, ImportExportModelAdmin)
#### Legistlative Assembly
class assemblypersonalAdmin(admin.ModelAdmin):
    search_fields = ('mla',)
admin.site.register(assemblypersonal, assemblypersonalAdmin)
'''class assemblyAdmin(admin.ModelAdmin):
    search_fields = ('MLA_name',)
admin.site.register(Legislative_Assembly,assemblyAdmin)'''
admin.site.register(Legislative_Assembly, ImportExportModelAdmin)

#### Legistlative Council
class councilpersonalAdmin(admin.ModelAdmin):
    search_fields = ('mlc',)
#admin.site.register(councilpersonal, councilpersonalAdmin)
'''class councilAdmin(admin.ModelAdmin):
    search_fields = ('MLC_name',)
admin.site.register(Legislative_councils, councilAdmin)'''
admin.site.register(Legislative_councils, ImportExportModelAdmin)
admin.site.register(councilpersonal)
admin.site.register(Legislative_Council_Presence, ImportExportModelAdmin)

admin.site.register(Assembly_time_period, ImportExportModelAdmin)

admin.site.register(Panchayat_time_period, ImportExportModelAdmin)

admin.site.register(Municipal_corporation_time_period, ImportExportModelAdmin)

admin.site.register(State, ImportExportModelAdmin)

admin.site.register(Districts, ImportExportModelAdmin)

admin.site.register(City, ImportExportModelAdmin)

admin.site.register(Collector, ImportExportModelAdmin)

admin.site.register(Assembly_Constituency, ImportExportModelAdmin)

admin.site.register(Grama_panchayat, ImportExportModelAdmin)

admin.site.register(Corporation, ImportExportModelAdmin)

admin.site.register(Panchayat_Ward_Number, ImportExportModelAdmin)

admin.site.register(Corporation_Ward_Number, ImportExportModelAdmin)

admin.site.register(PM, ImportExportModelAdmin)

admin.site.register(President, ImportExportModelAdmin)

admin.site.register(Vice_President, ImportExportModelAdmin)

admin.site.register(Rajyasabha_Chairman, ImportExportModelAdmin)

admin.site.register(Loksabha_Chairman, ImportExportModelAdmin)



admin.site.register(Rajyasabha_Complete_Session, ImportExportModelAdmin)

admin.site.register(Current_Prime_Minister, ImportExportModelAdmin)

admin.site.register(Current_President, ImportExportModelAdmin)

admin.site.register(Current_Vice_President, ImportExportModelAdmin)

admin.site.register(Current_Loksabha_Speaker, ImportExportModelAdmin)

admin.site.register(Current_Loksabha_Deputy_Speaker, ImportExportModelAdmin)

admin.site.register(Current_Loksabha_Opposition_Leader, ImportExportModelAdmin)

admin.site.register(Current_Rajyasabha_House_Leader, ImportExportModelAdmin)

admin.site.register(Current_Rajyasabha_Deputy_Speaker, ImportExportModelAdmin)

admin.site.register(Current_Rajyasabha_Opposition_Leader, ImportExportModelAdmin)

admin.site.register(Flag, ImportExportModelAdmin)

admin.site.register(Sessions, ImportExportModelAdmin)

admin.site.register(Municipal_Corporation, ImportExportModelAdmin)

admin.site.register(Mayor, ImportExportModelAdmin)

admin.site.register(Corporator, ImportExportModelAdmin)

admin.site.register(Mannkibaat, ImportExportModelAdmin)
