from django.urls import path
from django.conf.urls import url,include

from . import views
#from .views import end_game

urlpatterns=[
    path('',views.index,name='Index'),
    url(r'^end-game/?',views.end_game, name='end-game'),
]