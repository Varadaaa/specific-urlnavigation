from app1.views import *
from django.urls import path

app_name ='p'


urlpatterns=[
    path('python/', python, name='python'),
]