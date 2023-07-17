import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from menu import Menu


def play_game():
    if is_on_menu:
        start_game()


def start_game():
    global is_on_menu
    is_on_menu = False
    game_is_on = True
    menu.clear()
    scoreboard.print_scoreboard()
    loop_counter = 0
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.move()

        if player.is_finished():
            print('You win')
            level_up()

        if car_manager.collision(player):
            print('You lose')
            game_over()
            game_is_on = False

        if loop_counter % 6 == 0:
            car_manager.new_car()

        loop_counter += 1
        print(f'Number of cars: {len(car_manager.cars)}')


def restart_game():
    scoreboard.reset()
    player.reset()
    car_manager.reset()
    start_game()


def level_up():
    scoreboard.level_up()
    car_manager.level_up()
    player.reset()


def game_over():
    player.reset()
    car_manager.reset()
    scoreboard.print_gameover()


screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
is_on_menu = True

screen.listen()
screen.onkey(player.move_up, 'w')
screen.onkey(player.move_up, 'W')
screen.onkey(player.move_down, 's')
screen.onkey(player.move_down, 'S')
screen.onkey(player.move_left, 'a')
screen.onkey(player.move_left, 'A')
screen.onkey(player.move_right, 'd')
screen.onkey(player.move_right, 'D')
screen.onkey(restart_game, 'r')
screen.onkey(restart_game, 'R')
screen.onkey(play_game, 'p')
screen.onkey(play_game, 'P')

menu = Menu()

screen.exitonclick()
