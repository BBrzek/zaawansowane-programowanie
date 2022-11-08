from services.functions import csv_to_list

class Movie:
    def __init__(self, movieId: int, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres
    def __str__(self):
        return f"movieId: {self.movieId}, title: {self.title}, genres: {self.genres}"



movies_path = 'data/movies.csv'
list_movies = csv_to_list(movies_path)
list_of_movies = [Movie(list_movies[x][0], list_movies[x][1], list_movies[x][2]) for x in range(1, len(list_movies))]

