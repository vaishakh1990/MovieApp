from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.home, name = 'movies-home'),
    path('search/',views.find_movie, name = 'movies-search'),
    #url(r'detail/(?P<Title>[\w\W]+)$',views.get_details, name = 'movies-detail'),
    url('detail/',views.get_details, name = 'movies-detail'),
]
