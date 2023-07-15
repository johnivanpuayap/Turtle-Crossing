import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        for i in range(NUMBER_OF_CARS):
            self.cars.append(self.generate_car())

    def generate_car(self):
        car_color = random.choice(COLORS)
        car_position = (random.randint(280, 330), random.randint(-230, 230))
        car = Car(car_color, car_position)
        return car

    def move(self):
        for car in self.cars:
            car.move(self.speed)

            if car.xcor() < -330:
                car.hideturtle()
                self.cars.remove(car)

    def new_car(self):
        self.cars.append(self.generate_car())
