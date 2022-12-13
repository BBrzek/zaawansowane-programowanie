class Images:
    def __init__(self, image: str, num_of_people):
        self.image = image
        self.num_of_people = num_of_people

    def __str__(self):
        print(f'Image: {self.image} | num of people: {self.num_of_people}')