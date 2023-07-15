from turtle import Turtle

class Car(Turtle):

    def __init__(self, car_color, car_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(stretch_len=2)
        self.color(car_color)
        self.goto(car_position)

    def move(self, speed):
        self.forward(speed)