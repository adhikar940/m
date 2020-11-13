from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register your models here.
admin.site.register(Movie, ImportExportModelAdmin)

admin.site.register(BiharCandidate, ImportExportModelAdmin)

admin.site.register(BiharWinners, ImportExportModelAdmin)

admin.site.register(BiharRunners, ImportExportModelAdmin)

admin.site.register(DubbakaCandidate, ImportExportModelAdmin)

admin.site.register(DubbakaWinners, ImportExportModelAdmin)

admin.site.register(DubbakaRunners, ImportExportModelAdmin)

admin.site.register(Bihar_Coalition_Party, ImportExportModelAdmin)

admin.site.register(Party, ImportExportModelAdmin)

admin.site.register(LeadingSeats, ImportExportModelAdmin)

admin.site.register(Parliament, ImportExportModelAdmin)
admin.site.register(RajyaSabha, ImportExportModelAdmin)
admin.site.register(LokSabha, ImportExportModelAdmin)
admin.site.register(AndhraPradesh, ImportExportModelAdmin)
admin.site.register(ArunachalPradesh, ImportExportModelAdmin)

admin.site.register(Assam, ImportExportModelAdmin)
admin.site.register(Bihar, ImportExportModelAdmin)
admin.site.register(Chhattishgarh, ImportExportModelAdmin)
admin.site.register(Goa, ImportExportModelAdmin)
admin.site.register(Gujarat, ImportExportModelAdmin)
admin.site.register(Haryana, ImportExportModelAdmin)
admin.site.register(HimachalPradesh, ImportExportModelAdmin)
admin.site.register(JammuandKashmir, ImportExportModelAdmin)
admin.site.register(Jharkhand, ImportExportModelAdmin)
admin.site.register(Karnataka, ImportExportModelAdmin)
admin.site.register(Kerala, ImportExportModelAdmin)
admin.site.register(MadhyaPradesh, ImportExportModelAdmin)
admin.site.register(Meghalaya, ImportExportModelAdmin)
admin.site.register(Maharashtra, ImportExportModelAdmin)
admin.site.register(Manipur, ImportExportModelAdmin)
admin.site.register(Mizoram, ImportExportModelAdmin)
admin.site.register(Nagaland, ImportExportModelAdmin)
admin.site.register(Odisha, ImportExportModelAdmin)
admin.site.register(Punjab, ImportExportModelAdmin)
admin.site.register(Rajasthan, ImportExportModelAdmin)
admin.site.register(Sikkim, ImportExportModelAdmin)
admin.site.register(TamilNadu, ImportExportModelAdmin)
admin.site.register(Telangana, ImportExportModelAdmin)
admin.site.register(Tripura, ImportExportModelAdmin)
admin.site.register(Uttarakhand, ImportExportModelAdmin)
admin.site.register(UttarPradesh, ImportExportModelAdmin)
admin.site.register(WestBengal, ImportExportModelAdmin)
admin.site.register(AndhraPradeshforRajyasabha, ImportExportModelAdmin)
admin.site.register(ArunachalPradeshforRajyasabha, ImportExportModelAdmin)

admin.site.register(AssamforRajyasabha, ImportExportModelAdmin)
admin.site.register(BiharforRajyasabha, ImportExportModelAdmin)
admin.site.register(ChhattishgarhforRajyasabha, ImportExportModelAdmin)
admin.site.register(GoaforRajyasabha, ImportExportModelAdmin)
admin.site.register(GujaratforRajyasabha, ImportExportModelAdmin)
admin.site.register(HaryanaforRajyasabha, ImportExportModelAdmin)
admin.site.register(HimachalPradeshforRajyasabha, ImportExportModelAdmin)
admin.site.register(JammuandKashmirforRajyasabha, ImportExportModelAdmin)
admin.site.register(JharkhandforRajyasabha, ImportExportModelAdmin)
admin.site.register(KarnatakaforRajyasabha, ImportExportModelAdmin)
admin.site.register(KeralaforRajyasabha, ImportExportModelAdmin)
admin.site.register(MadhyaPradeshforRajyasabha, ImportExportModelAdmin)
admin.site.register(MeghalayaforRajyasabha, ImportExportModelAdmin)
admin.site.register(MaharashtraforRajyasabha, ImportExportModelAdmin)
admin.site.register(ManipurforRajyasabha, ImportExportModelAdmin)
admin.site.register(MizoramforRajyasabha, ImportExportModelAdmin)
admin.site.register(NagalandforRajyasabha, ImportExportModelAdmin)
admin.site.register(OdishaforRajyasabha, ImportExportModelAdmin)
admin.site.register(PunjabforRajyasabha, ImportExportModelAdmin)
admin.site.register(RajasthanforRajyasabha, ImportExportModelAdmin)
admin.site.register(SikkimforRajyasabha, ImportExportModelAdmin)
admin.site.register(TamilNaduforRajyasabha, ImportExportModelAdmin)
admin.site.register(TelanganaforRajyasabha, ImportExportModelAdmin)
admin.site.register(TripuraforRajyasabha, ImportExportModelAdmin)
admin.site.register(UttarakhandforRajyasabha, ImportExportModelAdmin)
admin.site.register(UttarPradeshforRajyasabha, ImportExportModelAdmin)
admin.site.register(WestBengalforRajyasabha, ImportExportModelAdmin)
