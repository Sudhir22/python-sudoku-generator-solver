from django.urls import path
from django.conf.urls import url,include

from . import views
#from .views import end_game

urlpatterns=[
    path('sudoku_solver/',views.index,name='Index'),
    path('homepage/',views.homepage,name='homepage'),
    url(r'^end-game/?',views.end_game, name='end-game'),
]