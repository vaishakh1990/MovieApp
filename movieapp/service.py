import requests
from django.conf import settings

def find_movie_detail(search_key):
    movie_list = list()
    #url = 'http://www.omdbapi.com/?t={0}&apikey=a43a80f'.format(search_key)
    url = settings.OMDB_URL + '?t={0}&apikey='.format(search_key) + settings.OMDB_API_KEY
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        if response.json()['Response'] == 'True':
            movie_details = {
                'poster_url': response.json()['Poster'],
                'title': response.json()['Title'],
                'year': response.json()['Year'],
                'plot': response.json()['Plot'],
                'imdbid' : response.json()['imdbID'],
                'rated' : response.json()['Rated'],
                'released' : response.json()['Released'],
                'genre' : response.json()['Genre'],
                'director' : response.json()['Director'],
                'language' : response.json()['Language'],
                'imdbrating' : response.json()['imdbRating'],
                'errorstatus': False
            }
        else:
            movie_details = {
                'error': response.json()['Error'],
                'errorstatus': True,
            }
        movie_list.append(movie_details)
    return movie_list


def find_movie_list(search_key):
    movie_list = list()
    #url = 'http://www.omdbapi.com/?s={0}&apikey=a43a80f'.format(search_key)
    url = settings.OMDB_URL + '?s={0}&apikey='.format(search_key) + settings.OMDB_API_KEY
    response = requests.get(url)
    if response.status_code == requests.codes.ok:
        if response.json()['Response'] == 'True':
            movie_list = response.json()['Search']
            movie_list.append({'errorstatus' : False})
        else:
            movie_list.append({
                'error': response.json()['Error'],
                'errorstatus': True,
            })
    return movie_list
