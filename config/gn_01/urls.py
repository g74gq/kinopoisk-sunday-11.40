from django.urls import path
from gn_01.views import *

urlpatterns = [
    path('', home, name='home'),
    path('movies_list/', movies_list, name='movies_list'),
    path('actors_list/', actors_list, name='actors_list'),
    path('directors_list/', directors_list, name='directors_list'),
    path('generes_list/', generes_list, name='generes_list'),
    path('composers_list/', composers_list, name='composers_list'),
    path('movie_detail/<int:movie_id>/', movies_detail, name='movie_detail'),
    path('actors_detail/<int:actors_id>/', actors_detail, name='actors_detail'),
    path('directors_detail/<int:directors_id>/', directors_detail, name='directors_detail'),
    path('generes_detail/<int:generes_id>/', generes_detail, name='generes_detail'),
    path('composers_detail/<int:composers_id>/', composers_detail, name='composters_detail'),
    path('add_movie_review/', add_movie_review, name='add_movie_review')
]