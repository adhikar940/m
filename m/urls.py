from django.urls import include, path
from django.conf.urls import url,include
from rest_framework import routers
from django.contrib import admin
from n import views
from django.conf.urls.static import static
from m import settings

router = routers.DefaultRouter()
router.register(r'movies', views.MovieViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include(router.urls)),
    path('n/',include('n.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

