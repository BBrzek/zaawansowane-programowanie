class Property:

    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"Area: {self.area}, rooms: {self.rooms}, price: {self.price}, address: {self.address}"


class House(Property):

    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return super().__str__() + f", plot: {self.plot}"


class Fiat(Property):

    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return super().__str__() + f", floor: {self.floor}"


house1 = House("aaa", 3, 3000, "Babushki", 400)
fiat1 = Fiat("bbb", 1, 3000, "Catcta", 999)
print(house1.__str__())
print(fiat1.__str__())
