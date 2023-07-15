import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_up, 'W')
screen.onkey(player.move_down, 's')
screen.onkey(player.move_down, 'S')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_left, 'A')
screen.onkey(player.move_right, 'd')
screen.onkey(player.move_right, 'D')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.is_finished():
        print('You win')
        break
