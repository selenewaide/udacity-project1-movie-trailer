# Movies class.
# Used to compile data for each movie.


class Movie():
    def __init__(self, movie_title, movie_data, youtube_video_id):
        self.title = movie_title
        self.storyline = movie_data['Plot']
        self.poster_image_url = movie_data['Poster']
        self.awards = movie_data['Awards']
        self.director = movie_data['Director']
        self.genre = movie_data['Genre']
        self.boxoffice = movie_data['BoxOffice']
        self.rated = movie_data['Rated']
        self.rating = movie_data['imdbRating']
        self.runtime = movie_data['Runtime']
        self.year = movie_data['Year']
        self.votes = movie_data['imdbVotes']
        self.actors = movie_data['Actors']
        self.trailer_youtube_id = youtube_video_id
