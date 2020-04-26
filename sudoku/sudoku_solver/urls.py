from django.urls import path
from django.conf.urls import url,include

from . import views
#from .views import end_game

urlpatterns=[
    path('sudoku_solver/',views.index,name='Index'),
    path('homepage/',views.homepage,name='homepage'),
    path('homepage_2/',views.homepage_2,name='homepage_2'),
    path('task/',views.task,name='task'),
    path('task_2/',views.task,name='task_2'),
    path('second_task/',views.second_task,name='second_task'),
    path('second_task_2/',views.second_task,name='second_task_2'),
    url(r'^end-game/?',views.end_game, name='end-game'),
] 