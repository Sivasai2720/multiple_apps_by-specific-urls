from rcb.views import *
from django.urls import path

urlpatterns=[
    path('kholi/',kholi,name='kholi'),
    path('abd/',abd,name='abd'),
]