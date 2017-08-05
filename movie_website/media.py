import webbrowser

class Movie():
    """ This class provides a way to score movie related information"""
    def __init__(self, movie_title, poster_image, youtube_trailer, movie_year, movie_rating):
        self.title = movie_title
        self.poster_image_url  = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.movie_year = movie_year
        self.movie_rating = movie_rating

    """show trailer function is for showing url in webbrowser"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
