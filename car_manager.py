import random
from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
STARTING_NUMBER_OF_CARS = 1


class CarManager:
    def __init__(self):
        self.cars = []
        self.number_of_cars = STARTING_NUMBER_OF_CARS
        self.speed = STARTING_MOVE_DISTANCE
        self.generate_cars()

    def generate_cars(self):
        for i in range(self.number_of_cars):
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
        for i in range(self.number_of_cars):
            self.cars.append(self.generate_car())

    def collision(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False

    def reset(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.number_of_cars = STARTING_NUMBER_OF_CARS

    def level_up(self):
        for car in self.cars:
            car.hideturtle()
            self.cars.remove(car)
        self.speed += MOVE_INCREMENT
        self.number_of_cars += 1
