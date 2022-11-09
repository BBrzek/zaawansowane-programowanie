from services.functions import csv_to_list

class Link:
    def __init__(self, movieId: int, imdbId: int, tmdbId: int):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId
    def __str__(self):
        return f"movieId: {self.movieId}, imdbId: {self.imdbId}, tmdbId: {self.tmdbId}"


links_path = 'data/links.csv'
list_links = csv_to_list(links_path)
list_of_links = [Link(list_links[x][0], list_links[x][1], list_links[x][2]) for x in range(1, len(list_links))]

