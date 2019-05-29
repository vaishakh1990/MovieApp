from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import MovieSearchForm
from movieapp.service import find_movie_list, find_movie_detail
from .models import Favourite
import json

def home(request):
    return render(request, 'movieapp/main.html')

def find_movie(request):
    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            search_key = form.cleaned_data.get('search')
            movie_list = find_movie_list(search_key)
            fav_list = list(Favourite.objects.filter(person_id = request.user).values('Imdbid'))
            for mov in movie_list:
                if any(d.get('Imdbid') == mov.get('imdbID') for d in fav_list):
                   id = movie_list.index(mov)
                   movie_list[id]['fav'] = 1
            return render(request,'movieapp/main.html',{ 'movie_lists': movie_list })
    else:
        form = MovieSearchForm()
        return render(request,'movieapp/main.html')

def get_details(request):
    id = request.GET.get('id')
    movie_details = find_movie_detail(id)
    return render(request,'movieapp/details.html', {'movie_details' : movie_details })

def save_favourite(request):
    title = request.GET.get('title')
    imdbid = request.GET.get('imdbid')
    year = request.GET.get('year')
    poster_url = request.GET.get('poster')
    fav_exist = Favourite.objects.filter(Imdbid = imdbid,person_id = request.user)
    if fav_exist:
        fav_exist.delete()
        data = {'status':0}
    else:
        fav = Favourite(person_id=request.user,Imdbid=imdbid,Year=year,Title=title,Poster=poster_url)
        tes = fav.save()
        data = {'status':1}
    return HttpResponse(json.dumps(data), content_type="application/json")

def list_fav(request):
    favlist = list(Favourite.objects.filter(person_id = request.user).values())
    return render(request,'movieapp/favourite_list.html',{'fav_lists': favlist})
