from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.print_scoreboard()

    def print_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.print_scoreboard()

    def print_gameover(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        self.goto(0, -20)
        self.write("Press 'R' or 'r' to play again", align="center", font=("Courier", 12, "normal"))

    def reset(self):
        self.clear()
        self.level = 1
        self.print_scoreboard()