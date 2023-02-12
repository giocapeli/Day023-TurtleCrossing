import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkeypress(player.move_forward, "w") #dont pass () to the function or it calls itself
screen.onkeypress(player.move_backward, "s")
screen.onkeypress(player.move_right, "d")
screen.onkeypress(player.move_left, "a")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    
screen.exitonclick()

