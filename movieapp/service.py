import requests
from django.conf import settings

# Gets the imdbID to be searched from the views , here we hit the OMDB url
# Passes the imdbID adn type movie along with  the API key
# The response is the details of the particular movie and is in a json format and is passed back to the views

def find_movie_detail(search_key):
    movie_list = list()
    url = settings.OMDB_URL + '?i={0}&type=movie&apikey='.format(search_key) + settings.OMDB_API_KEY
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        movie_list.append({
            'errorstatus' : False,
            'error': e,
        })
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
                'errorstatus': True
                }
        else:
            movie_details = {
                'error': response.json()['Error'],
                'errorstatus': False,
            }
        movie_list.append(movie_details)
    else:
        movie_list.append({
            'errorstatus': False,
            'error': response.json()['Error'],
        })
    return movie_list

# Gets the value to be searched from the views , here we hit the OMDB url
# Passes the search key adn type movie along with  the API key
# The response is in a json format and is passed back to the views

def find_movie_list(search_key):
    movie_list = list()
    url = settings.OMDB_URL + '?s={0}&type=movie&apikey='.format(search_key) + settings.OMDB_API_KEY
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        movie_list.append({
            'errorstatus' : False,
            'error': e,
        })
        return movie_list
    if response.status_code == requests.codes.ok:
        if response.json()['Response'] == 'True':
            movie_list = response.json()['Search']
            movie_list.append({'errorstatus' : True})
        else:
            movie_list.append({
                'errorstatus': False,
                'error': response.json()['Error'],
            })
    else:
        movie_list.append({
            'errorstatus': False,
            'error': response.json()['Error'],
        })
    return movie_list
