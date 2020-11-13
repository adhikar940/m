from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from n import views as user_views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

url(r'^bihar_api/',user_views.Bihar_api.as_view()),
url(r'^dubbakka_api/',user_views.Dubbaka_api.as_view()),
url(r'^dubbakkawinner_api/',user_views.DubbakaWinner_api.as_view()),
url(r'^dubbakkarunner_api/',user_views.DubbakaRunner_api.as_view()),
url(r'^biharwinner_api/',user_views.BiharWinner_api.as_view()),
url(r'^biharrunner_api/',user_views.BiharRunner_api.as_view()),
url(r'^party_api/',user_views.Party_api.as_view()),
url(r'^coalitionparty_api/',user_views.Coalition_Party_api.as_view()),
url(r'^leading_api/',user_views.Leadingseats_api.as_view()),


url(r'^AndhraPradeshrajyasabha_api/',user_views.AndhraPradeshrajyasabha_api.as_view()),
url(r'^AndhraPradeshloksabha_api/',user_views.AndhraPradeshloksabha_api.as_view()),

url(r'^ArunachalPradeshrajyasabha_api/',user_views.ArunachalPradeshrajyasabha_api.as_view()),
url(r'^ArunachalPradeshloksabha_api/',user_views.ArunachalPradeshloksabha_api.as_view()),

url(r'^Assamrajyasabha_api/',user_views.Assamrajyasabha_api.as_view()),
url(r'^Assamloksabha_api/',user_views.Assamloksabha_api.as_view()),

url(r'^Biharrajyasabha_api/',user_views.Biharrajyasabha_api.as_view()),
url(r'^Biharloksabha_api/',user_views.Biharloksabha_api.as_view()),

url(r'^Chhattishgarhrajyasabha_api/',user_views.Chhattishgarhrajyasabha_api.as_view()),
url(r'^Chhattishgarhloksabha_api/',user_views.Chhattishgarhloksabha_api.as_view()),

url(r'^Goarajyasabha_api/',user_views.Goarajyasabha_api.as_view()),
url(r'^Goaloksabha_api/',user_views.Goaloksabha_api.as_view()),

url(r'^Gujaratrajyasabha_api/',user_views.Gujaratrajyasabha_api.as_view()),
url(r'^Gujaratloksabha_api/',user_views.Gujaratloksabha_api.as_view()),

url(r'^Haryanarajyasabha_api/',user_views.Haryanarajyasabha_api.as_view()),
url(r'^Haryanaloksabha_api/',user_views.Haryanaloksabha_api.as_view()),

url(r'^HimachalPradeshrajyasabha_api/',user_views.HimachalPradeshrajyasabha_api.as_view()),
url(r'^HimachalPradeshloksabha_api/',user_views.HimachalPradeshloksabha_api.as_view()),

url(r'^JammuandKashmirrajyasabha_api/',user_views.JammuandKashmirrajyasabha_api.as_view()),
url(r'^JammuandKashmirloksabha_api/',user_views.JammuandKashmirloksabha_api.as_view()),

url(r'^Jharkhandrajyasabha_api/',user_views.Jharkhandrajyasabha_api.as_view()),
url(r'^Jharkhandloksabha_api/',user_views.Jharkhandloksabha_api.as_view()),

url(r'^Karnatakarajyasabha_api/',user_views.Karnatakarajyasabha_api.as_view()),
url(r'^Karnatakaloksabha_api/',user_views.Karnatakaloksabha_api.as_view()),

url(r'^Keralarajyasabha_api/',user_views.Keralarajyasabha_api.as_view()),
url(r'^Keralaloksabha_api/',user_views.Keralaloksabha_api.as_view()),

url(r'^MadhyaPradeshrajyasabha_api/',user_views.MadhyaPradeshrajyasabha_api.as_view()),
url(r'^MadhyaPradeshloksabha_api/',user_views.MadhyaPradeshloksabha_api.as_view()),

url(r'^Maharashtrarajyasabha_api/',user_views.Maharashtrarajyasabha_api.as_view()),
url(r'^Maharashtraloksabha_api/',user_views.Maharashtraloksabha_api.as_view()),

url(r'^Manipurrajyasabha_api/',user_views.Manipurrajyasabha_api.as_view()),
url(r'^Manipurloksabha_api/',user_views.Manipurloksabha_api.as_view()),

url(r'^Meghalayarajyasabha_api/',user_views.Meghalayarajyasabha_api.as_view()),
url(r'^Meghalayaloksabha_api/',user_views.Meghalayaloksabha_api.as_view()),

url(r'^Mizoramrajyasabha_api/',user_views.Mizoramrajyasabha_api.as_view()),
url(r'^Mizoramloksabha_api/',user_views.Mizoramloksabha_api.as_view()),

url(r'^Nagalandrajyasabha_api/',user_views.Nagalandrajyasabha_api.as_view()),
url(r'^Nagalandloksabha_api/',user_views.Nagalandloksabha_api.as_view()),

url(r'^Odisharajyasabha_api/',user_views.Odisharajyasabha_api.as_view()),
url(r'^Odishaloksabha_api/',user_views.Odishaloksabha_api.as_view()),

url(r'^Punjabrajyasabha_api/',user_views.Punjabrajyasabha_api.as_view()),
url(r'^Punjabloksabha_api/',user_views.Punjabloksabha_api.as_view()),

url(r'^Rajasthanrajyasabha_api/',user_views.Rajasthanrajyasabha_api.as_view()),
url(r'^Rajasthanloksabha_api/',user_views.Rajasthanloksabha_api.as_view()),

url(r'^Sikkimrajyasabha_api/',user_views.Sikkimrajyasabha_api.as_view()),
url(r'^Sikkimloksabha_api/',user_views.Sikkimloksabha_api.as_view()),

url(r'^TamilNadurajyasabha_api/',user_views.TamilNadurajyasabha_api.as_view()),
url(r'^TamilNaduloksabha_api/',user_views.TamilNaduloksabha_api.as_view()),

url(r'^Telanganarajyasabha_api/',user_views.Telanganarajyasabha_api.as_view()),
url(r'^Telanganaloksabha_api/',user_views.Telanganaloksabha_api.as_view()),

url(r'^Tripurarajyasabha_api/',user_views.Tripurarajyasabha_api.as_view()),
url(r'^Tripuraloksabha_api/',user_views.Tripuraloksabha_api.as_view()),

url(r'^UttarPradeshrajyasabha_api/',user_views.UttarPradeshrajyasabha_api.as_view()),
url(r'^UttarPradeshloksabha_api/',user_views.UttarPradeshloksabha_api.as_view()),

url(r'^Uttarakhandrajyasabha_api/',user_views.Uttarakhandrajyasabha_api.as_view()),
url(r'^Uttarakhandloksabha_api/',user_views.Uttarakhandloksabha_api.as_view()),

url(r'^WestBengalrajyasabha_api/',user_views.WestBengalrajyasabha_api.as_view()),
url(r'^WestBengalloksabha_api/',user_views.WestBengalloksabha_api.as_view()),




url(r'^states_api/', user_views.States_api.as_view()),
]