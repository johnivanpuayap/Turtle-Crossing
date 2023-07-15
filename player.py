from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.setheading(90)
        self.shape('turtle')
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())

    def is_finished(self):
        return self.ycor() == FINISH_LINE_Y
