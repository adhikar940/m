from django.urls import include, path
from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from n import views
from django.conf.urls.static import static
from m import settings
from rest_framework.authtoken.views import obtain_auth_token
#from rest_framework.authtoken import views
from django.contrib.auth import views as auth_views
from n.views import ChangePasswordView

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('user1', views.User1ViewSet)
router.register('party', views.PartyViewSet,basename='party')
#router.register('stateparty', views.statePartyViewSet)
router.register('lokperson', views.loksabhapersonalViewSet,basename='lok')
router.register('rajperson', views.rajyasabhapersonalViewSet,basename='raj')
router.register('rajpersonal', views.rajyasabhapersonal1ViewSet,basename='raj1')
router.register('assemblyperson', views.assemblypersonalViewSet,basename='assembly')
router.register('councilperson', views.councilpersonalViewSet,basename='council')
router.register('rajpersondisplay', views.rajpersonalViewSet,basename='r')
router.register('councilpersondisplay', views.CouncilpersonalViewSet,basename='c')
router.register('lokpersondisplay', views.LoksabhapersonalViewSet,basename='l')
router.register('assemblypersondisplay', views.AssemblypersonalViewSet,basename='a')
#router.register('Ll', views.LlViewSet)
#urlpatterns = router.urls


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
path('loksabha/', include('loksabha.urls')),
path('rajyasabha/', include('rajyasabha.urls')),
path('assembly/', include('assembly.urls')),
path('council/', include('council.urls')),
path('party/', include('party.urls')),
path('auth/', obtain_auth_token),
url('authenticate/', views.CustomObtainAuthToken.as_view()),
 path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
 path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('admin/',admin.site.urls),
path('', include(router.urls)),
    path('n/',include('n.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('login/', views.user_login, name='login'),
    path('p/', views.p, name='p'),
    path('partylogin/', views.party_login, name='partylogin'),
    path('profile/', views.profile, name='profile'),
    path('partyprofile/', views.partyprofile, name='partyprofile'),
    #path('password_mla/', views.passwordcreatetwo, name='mlapassword'),
    path('password_success/', views.passwordsuccess, name='success'),
    #url(r'^password_mla/(?P<party>)/$',views.passwordcreation,name='mlapassword'),
    #url(r'^password_mla/(?P<party>\w+)/(?P<MLA_name>)/$', views.passwordcreation, name='mlapassword'),
    path('postuserinfo/', views.model_form_upload, name='postuserinfo'),
    path('updateuserinfo/', views.update_user_info, name='updateuserinfo'),
    path('', views.user_logout, name='logout'),
    path('partylogout/', views.party_logout, name='partylogout'),
    path('change_password/', views.user_change_password, name='changepassword'),
    path('forgot_password/', views.user_forgot_password, name='forgotpassword'),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name= "n/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="n/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="n/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="n/password_reset_done.html"),
         name="password_reset_complete"),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


path('', include(router.urls)),
