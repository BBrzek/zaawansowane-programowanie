#userId,movieId,tag,timestamp
from services.functions import csv_to_list

class Tags:
    def __init__(self, userId: int, movieId: int, tag: str, timestamp: str):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp
    def __str__(self):
        return f"userId: {self.userId}, movieId: {self.movieId}, tag: {self.tag}, timestamp: {self.timestamp}"


tags_path = 'data/tags.csv'
list_tags = csv_to_list(tags_path)
list_of_tags = [Tags(list_tags[x][0], list_tags[x][1], list_tags[x][2], list_tags[x][3]) for x in range(1, len(list_tags))]

