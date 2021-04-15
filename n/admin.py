from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(PartyMemberPassword, ImportExportModelAdmin)

admin.site.register(PartywiseMP, ImportExportModelAdmin)

admin.site.register(PartywiseMLA, ImportExportModelAdmin)

admin.site.register(Loksabha_Session, ImportExportModelAdmin)

admin.site.register(Rajyasabha_Session, ImportExportModelAdmin)

admin.site.register(Legislative_Assembly_Session, ImportExportModelAdmin)

admin.site.register(Legislative_council_Session, ImportExportModelAdmin)

admin.site.register(user_profile, ImportExportModelAdmin)

admin.site.register(Movie, ImportExportModelAdmin)

admin.site.register(BiharCandidate, ImportExportModelAdmin)

admin.site.register(BiharWinners, ImportExportModelAdmin)

admin.site.register(BiharRunners, ImportExportModelAdmin)

admin.site.register(DubbakaCandidate, ImportExportModelAdmin)

admin.site.register(DubbakaWinners, ImportExportModelAdmin)

admin.site.register(DubbakaRunners, ImportExportModelAdmin)

admin.site.register(Bihar_Coalition_Party, ImportExportModelAdmin)

admin.site.register(Party, ImportExportModelAdmin)

admin.site.register(States, ImportExportModelAdmin)

admin.site.register(LeadingSeats, ImportExportModelAdmin)

admin.site.register(Rajyasabha, ImportExportModelAdmin)

admin.site.register(LokSabha, ImportExportModelAdmin)

admin.site.register(Legislative_Assembly, ImportExportModelAdmin)

admin.site.register(Legislative_councils, ImportExportModelAdmin)

admin.site.register(Legislative_Council_Presence, ImportExportModelAdmin)

admin.site.register(Assembly_time_period, ImportExportModelAdmin)

admin.site.register(Panchayat_time_period, ImportExportModelAdmin)

admin.site.register(Municipal_corporation_time_period, ImportExportModelAdmin)

admin.site.register(State, ImportExportModelAdmin)

admin.site.register(Districts, ImportExportModelAdmin)

admin.site.register(City, ImportExportModelAdmin)

admin.site.register(Grama_panchayat, ImportExportModelAdmin)

admin.site.register(Corporation, ImportExportModelAdmin)

admin.site.register(Panchayat_Ward_Number, ImportExportModelAdmin)

admin.site.register(Corporation_Ward_Number, ImportExportModelAdmin)

admin.site.register(PM, ImportExportModelAdmin)

admin.site.register(President, ImportExportModelAdmin)

admin.site.register(Vice_President, ImportExportModelAdmin)

admin.site.register(Rajyasabha_Chairman, ImportExportModelAdmin)

admin.site.register(Loksabha_Chairman, ImportExportModelAdmin)

admin.site.register(Loksabha_Complete_Session, ImportExportModelAdmin)

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

admin.site.register(Parliamentary_Loksabha_Sessions, ImportExportModelAdmin)

admin.site.register(Parliamentary_Rajyasabha_Sessions, ImportExportModelAdmin)

admin.site.register(Municipal_Corporation, ImportExportModelAdmin)

admin.site.register(Mayor, ImportExportModelAdmin)

admin.site.register(Corporator, ImportExportModelAdmin)
