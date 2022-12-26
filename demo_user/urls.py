from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('', views.home, name='home'),
    path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]