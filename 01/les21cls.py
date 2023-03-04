class Car:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, item):
        return self.cars[item]

    def __repr__(self):
        return f'<Car {self.cars}>'

    def __str__(self):
        return f'Car with {len(self)} cars'

ford = Car()
ford.cars.append('Ferari')

print(ford)

