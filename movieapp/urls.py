from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home, name = 'movies-home'),
    path('search/',views.find_movie, name = 'movies-search'),
    url('detail/',views.get_details, name = 'movies-detail'),
    url('favourite/',views.save_favourite, name = 'movies-favourite'),
    #url('listfavourite/',views.list_favourite, name = 'movies-listfavourite'),
    url('listfav/',views.list_fav, name='movies-listfav'),
]
