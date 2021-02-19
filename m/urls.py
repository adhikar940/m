from django.urls import include, path
from django.conf.urls import url,include
from rest_framework import routers
from django.contrib import admin
from n import views
from django.conf.urls.static import static
from m import settings
from django.contrib.auth import views as auth_views

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/',admin.site.urls),
    url(r'^', include(router.urls)),
    path('n/',include('n.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.user_login, name='login'),
    path('partylogin/', views.party_login, name='partylogin'),
    path('profile/', views.profile, name='profile'),
    path('partyprofile/', views.partyprofile, name='partyprofile'),
    #path('password_mla/', views.passwordcreatetwo, name='mlapassword'),
    path('password_success/', views.passwordsuccess, name='success'),
    #url(r'^password_mla/(?P<party>)/$',views.passwordcreation,name='mlapassword'),
    #url(r'^password_mla/(?P<party>\w+)/(?P<MLA_name>)/$', views.passwordcreation, name='mlapassword'),
    path('postuserinfo/', views.model_form_upload, name='postuserinfo'),
    path('updateuserinfo/', views.update_user_info, name='updateuserinfo'),
    path('logout/', views.user_logout, name='logout'),
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