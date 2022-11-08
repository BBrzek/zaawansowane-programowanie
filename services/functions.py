import csv

def csv_to_list(path: str) -> list:
    with open(path, encoding='UTF-8') as file:
        movies = csv.reader(file)
        return [x for x in movies]
