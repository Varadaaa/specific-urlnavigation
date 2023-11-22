from app2.views import *

from django.urls import path

app_name='j'


urlpatterns=[
    path('java/', java, name='java'),
]