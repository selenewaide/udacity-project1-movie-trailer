# Get api data from youtube and ombd.
# Create a movie object list with trivia and youtube trailer url.
# Use fresh_tomatoes file to render a web page.


import fresh_tomatoes
import media
import requests


movie_names_file = 'data/movie_names.txt'
keys_file = 'data/keys.txt'


def get_data_list_from_file(file_name):
    '''
    Read a file by line.
    Return a list of lines as strings.
    '''
    data_list = []
    with open(file_name) as f:
        data_list = f.readlines()
        # Remove whitespace characters like `\n` at the end of each line.
        data_list = [x.strip() for x in data_list] 
    return data_list


def get_data_from_api(url):
    '''
    Get api data and return a python object.
    '''
    response = requests.get(url)
    data = response.json()
    return data


def get_movie_list():
    '''
    Creates a list movies with trivia and youtube trailer url.
    '''

    # Get api keys and movie names from files.
    keys = get_data_list_from_file(keys_file)
    youtube_key = keys[0]
    omdb_key = keys[1]
    movie_names = get_data_list_from_file(movie_names_file)

    # Compiles a list of movie objects using Youtube and OMDB APIs
    movie_list = []
    for movie_name in movie_names:
        # Get data from Youtube and OMDB using APIs
        search_phrase = movie_name.replace(" ", "+")
        omdb_url = "http://www.omdbapi.com/?t=" + \
            search_phrase + \
            "&plot=full&apikey=" + omdb_key
        youtube_url = "https://www.googleapis.com/youtube" \
            "/v3/search?part=id&q=" + search_phrase + "+trailer" \
            "&type=video&key=" + youtube_key
        omdb_data = get_data_from_api(omdb_url)
        youtube_data = get_data_from_api(youtube_url)
        youtube_video_id = str(youtube_data['items'][0]['id']['videoId'])

        # Create a movie object and add to movie_list
        movie = media.Movie(movie_name, omdb_data, youtube_video_id)
        movie_list.append(movie)
    return movie_list


if __name__ == "__main__":
    movies = get_movie_list()
    fresh_tomatoes.open_movies_page(movies)
