from django.urls import include, path
from . import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
#path('present_pm/',views.present_pm),
#path('all_pms/',views.all_pm)
#path('upload_image/',views.upload_image),
# Only a single URL to access GraphQL
#path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema))

]
