from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import MovieSearchForm
from movieapp.service import find_movie_list, find_movie_detail

def home(request):
    return render(request, 'movieapp/main.html')

def find_movie(request):
    if request.method == 'POST':
        form = MovieSearchForm(request.POST)
        if form.is_valid():
            search_key = form.cleaned_data.get('search')
            movie_list = find_movie_list(search_key)
            return render(request,'movieapp/main.html',{ 'movie_lists': movie_list })
    else:
        form = MovieSearchForm()
        return render(request,'movieapp/main.html')

def get_details(request):
    Title = request.GET.get('title')
    movie_details = find_movie_detail(Title)
    return render(request,'movieapp/details.html', {'movie_details' : movie_details })
