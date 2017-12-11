import fresh_tomatoes
import media
import requests

movie_list = []

movie_names = [
                'Rogue One',
                'Blade Runner 2049',
                'Guardians of the Galaxy Vol 2',
                'Despicable Me',
                'Avatar',
                'Cloud Atlas',
                'Million Dollar Baby',
                'Man on Wire',
                'Skyfall',
                'Coraline',
                'Ex Machina',
                'MirrorMask'
                ]


# Get api data and return python object.
def get_data(url):
    response = requests.get(url)
    data = response.json()
    return data


# Compiles a list of movie objects using Youtube and OMDB APIs
for movie_name in movie_names:
    # Get data from Youtube and OMDB using APIs
    search_phrase = movie_name.replace(" ", "+")
    omdb_url = "http://www.omdbapi.com/?t=" + \
        search_phrase + \
        "&plot=full&apikey=91e5994d"
    youtube_url = "https://www.googleapis.com/youtube" \
        "/v3/search?part=id&q=" + search_phrase + "+trailer" \
        "&type=video&key=AIzaSyB3jgnMCyjStgp1b1r1x9NMRE9NPvtA5Fw"
    omdb_data = get_data(omdb_url)
    youtube_data = get_data(youtube_url)
    youtube_video_id = str(youtube_data['items'][0]['id']['videoId'])

    # Create a movie object and add to movie_list
    movie = media.Movie(movie_name, omdb_data, youtube_video_id)
    movie_list.append(movie)


fresh_tomatoes.open_movies_page(movie_list)
