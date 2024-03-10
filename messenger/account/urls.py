from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from . import views

from .schema import schema

app_name = 'account'
urlpatterns = [
    path('wa_webhook', views.webhook, name='webhook'),
    path('send/<int:message_id>/', views.send_message_test, name='send_message'),
    path('home/', views.home_page, name='home_page'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
