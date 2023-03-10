import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
cars = CarManager()
road = Road()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forward, "w") #dont pass () to the function or it calls itself
screen.onkeypress(player.move_backward, "s")
screen.onkeypress(player.move_right, "d")
screen.onkeypress(player.move_left, "a")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    cars.create_car()
    cars.move()
    
    for car in cars.all_cars:
        if player.distance(car) <= 20:
            game_is_on = False
            score.game_over()
    
    if player.ycor() > road.other_side_y + 20:
        score.increasse()
        player.refresh()
        cars.speedup()
    
screen.exitonclick()

