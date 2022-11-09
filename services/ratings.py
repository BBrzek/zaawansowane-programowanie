from services.functions import csv_to_list

class Rating:
    def __init__(self, userId: int, movieId: int, rating: float, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp
    def __str__(self):
        return f"userId: {self.userId}, movieId: {self.movieId}, rating: {self.rating}, timestamp: {self.timestamp}"


ratings_path = 'data/ratings.csv'
list_ratings = csv_to_list(ratings_path)
list_of_ratings = [Rating(list_ratings[x][0], list_ratings[x][1], list_ratings[x][2], list_ratings[x][3]) for x in range(1, len(list_ratings))]

