from turtle import Turtle


class Menu(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.draw_menu()

    def draw_menu(self):
        self.goto(0, 240)
        self.write(f"Spade Productions", True, align="center", font=("Courier", 20, "normal"))

        self.goto(0, 0)
        self.write(f"Turtle Crossing", True, align="center", font=("Courier", 40, "normal"))

        self.goto(0, -200)
        self.write(f"Press 'p' or 'P' to start Playing", True, align="center", font=("Courier", 12, "normal"))
        self.hideturtle()

    def clear_menu(self):
        self.clear()