from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        
    def create_car(self):
        car = Turtle("square")
        car.shapesize(1, 2)
        car.penup()
        car.color(choice(COLORS))
        car.goto(300, randint(-250, 250))
        car.setheading(180)
        self.all_cars.append(car)
    
    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)